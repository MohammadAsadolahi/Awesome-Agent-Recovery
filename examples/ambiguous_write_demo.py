"""Offline simulation of an external write followed by a lost response.

No real transaction or external service is invoked.
"""
from dataclasses import dataclass, field


class AmbiguousTimeout(TimeoutError):
    """The remote effect may have committed before response loss."""


@dataclass
class FakeService:
    records: list[tuple[str, int]] = field(default_factory=list)
    operations: dict[str, tuple[str, int]] = field(default_factory=dict)
    drop_next_response: bool = True

    def _respond(self):
        if self.drop_next_response:
            self.drop_next_response = False
            raise AmbiguousTimeout("Write committed; response lost")

    def unsafe_write(self, account: str, cents: int):
        self.records.append((account, cents))
        self._respond()

    def idempotent_write(self, account: str, cents: int, key: str):
        payload = (account, cents)
        if key in self.operations:
            if self.operations[key] != payload:
                raise ValueError("Idempotency key reused with different payload")
            return
        self.records.append(payload)
        self.operations[key] = payload
        self._respond()

    def committed(self, key: str) -> bool:
        return key in self.operations


def blind_retry() -> FakeService:
    service = FakeService()
    try:
        service.unsafe_write("example", 100)
    except AmbiguousTimeout:
        service.unsafe_write("example", 100)
    return service


def reconcile_then_retry() -> FakeService:
    service = FakeService()
    operation_id = "invoice:123:create"
    try:
        service.idempotent_write("example", 100, operation_id)
    except AmbiguousTimeout:
        if not service.committed(operation_id):
            service.idempotent_write("example", 100, operation_id)
    return service


if __name__ == "__main__":
    unsafe = blind_retry()
    safe = reconcile_then_retry()
    print(f"Blind retry: {len(unsafe.records)} writes (UNSAFE)")
    print(f"Reconciliation + stable key: {len(safe.records)} write (SAFE in this simulator)")
    assert len(unsafe.records) == 2 and len(safe.records) == 1
    print("Simulation passed. Real API guarantees must be evaluated separately.")
