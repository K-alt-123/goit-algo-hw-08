from functools import lru_cache
import itertools
import random
import unittest

from solution import insert, find_minimum, sum_values, minimum_connection_cost


@lru_cache(None)
def exhaustive_cost(lengths):
    if len(lengths) < 2:
        return 0
    candidates = []
    for i, j in itertools.combinations(range(len(lengths)), 2):
        merged = lengths[i] + lengths[j]
        remainder = tuple(sorted([value for k, value in enumerate(lengths) if k not in (i, j)] + [merged]))
        candidates.append(merged + exhaustive_cost(remainder))
    return min(candidates)


class TreeAndHeapTests(unittest.TestCase):
    def test_tree_minimum_and_sum(self):
        for values in ([], [8], [5, -3, 9, -3, 2, 5], list(range(1200))):
            root = None
            for value in values:
                root = insert(root, value)
            self.assertEqual(find_minimum(root), min(values) if values else None)
            self.assertEqual(sum_values(root), sum(values))

    def test_cable_example_and_edges(self):
        self.assertEqual(minimum_connection_cost([4, 3, 2, 6]), 29)
        self.assertEqual(minimum_connection_cost([]), 0)
        self.assertEqual(minimum_connection_cost([10]), 0)
        self.assertEqual(minimum_connection_cost([0, 0, 0]), 0)
        for invalid in ([-1], [1.5], [True], ['2']):
            with self.assertRaises(ValueError):
                minimum_connection_cost(invalid)

    def test_heap_against_exhaustive_merge_orders(self):
        rng = random.Random(8)
        for size in range(7):
            for _ in range(10):
                lengths = [rng.randrange(7) for _ in range(size)]
                original = lengths.copy()
                self.assertEqual(minimum_connection_cost(lengths), exhaustive_cost(tuple(sorted(lengths))))
                self.assertEqual(lengths, original)


if __name__ == '__main__':
    unittest.main()
