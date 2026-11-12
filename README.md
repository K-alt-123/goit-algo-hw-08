# Trees and heaps

Python 3.12+; no third-party dependencies.

```powershell
python solution.py --help
python solution.py
python solution.py --tree-values 7 3 9 3 --cables 4 3 2 6
python solution.py --tree-values --cables
python -m unittest discover -s tests -v
```

## Binary search tree

`insert(root, value)` returns the tree root. Smaller values go left; equal and larger values go right, so duplicates contribute separately to the sum. `find_minimum` follows left links, taking O(h) time and O(1) space. The minimum of an empty tree is `None`.

`sum_values` visits every node using an explicit stack: O(n) time and O(h) stack space. An empty tree sums to zero. The default tree has minimum -3 and sum 15. This tree is not balanced: a sequence of ordered insertions can produce height n. Traversal is iterative to avoid Python recursion-limit failures on such trees.

## Cable connection cost

Each connection costs the sum of the two cable lengths. `minimum_connection_cost` heapifies a copy of the input, repeatedly removes the two shortest cables, adds their combined length to the total, and returns the new cable to the heap. The caller's list is unchanged.

For `[4, 3, 2, 6]`, the connections cost 5, 9, and 15: total **29**. Empty and one-cable lists cost zero. Negative, fractional, Boolean, and string lengths are rejected.

Choosing the two smallest cables first keeps their repeated contribution low; this is the optimal-merge pattern used by Huffman construction. Heap construction is O(n), and the subsequent merges take O(n log n) time with O(n) storage. Tests independently enumerate every merge choice for small cases rather than comparing the function with another heap implementation.
