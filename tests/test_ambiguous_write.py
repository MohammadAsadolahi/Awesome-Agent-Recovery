"""Tests for the dependency-free ambiguous-write simulation."""
import unittest

from examples.ambiguous_write_demo import (
    AmbiguousTimeout, FakeService, blind_retry, reconcile_then_retry
)


class RecoveryTests(unittest.TestCase):
    def test_unsafe_retry_duplicates(self):
        self.assertEqual(len(blind_retry().records), 2)

    def test_reconcile_does_not_duplicate(self):
        self.assertEqual(len(reconcile_then_retry().records), 1)

    def test_stable_key_prevents_duplicate(self):
        s = FakeService(drop_next_response=False)
        s.idempotent_write("a", 100, "k")
        s.idempotent_write("a", 100, "k")
        self.assertEqual(len(s.records), 1)

    def test_key_payload_conflict_rejected(self):
        s = FakeService(drop_next_response=False)
        s.idempotent_write("a", 100, "k")
        with self.assertRaises(ValueError):
            s.idempotent_write("b", 100, "k")

    def test_timeout_does_not_mean_failure(self):
        s = FakeService()
        with self.assertRaises(AmbiguousTimeout):
            s.idempotent_write("a", 100, "k")
        self.assertTrue(s.committed("k"))


if __name__ == "__main__":
    unittest.main()
