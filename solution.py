"""BST minimum/sum and minimum-cost cable connections with a min-heap."""
import argparse
from dataclasses import dataclass
import heapq


@dataclass
class Node:
    value: int
    left: 'Node | None' = None
    right: 'Node | None' = None


def insert(root: Node | None, value: int) -> Node:
    if root is None:
        return Node(value)
    node = root
    while True:
        direction = 'left' if value < node.value else 'right'
        child = getattr(node, direction)
        if child is None:
            setattr(node, direction, Node(value))
            break
        node = child
    return root


def find_minimum(root: Node | None) -> int | None:
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root.value


def sum_values(root: Node | None) -> int:
    total = 0
    pending = [root] if root is not None else []
    while pending:
        node = pending.pop()
        total += node.value
        if node.right is not None:
            pending.append(node.right)
        if node.left is not None:
            pending.append(node.left)
    return total


def minimum_connection_cost(lengths: list[int]) -> int:
    if any(type(length) is not int or length < 0 for length in lengths):
        raise ValueError('Cable lengths must be nonnegative integers')
    heap = list(lengths)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        merged = heapq.heappop(heap) + heapq.heappop(heap)
        total += merged
        heapq.heappush(heap, merged)
    return total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tree-values', type=int, nargs='*', default=[5, -3, 9, -3, 2, 5])
    parser.add_argument('--cables', type=int, nargs='*', default=[4, 3, 2, 6])
    args = parser.parse_args()
    root = None
    for value in args.tree_values:
        root = insert(root, value)
    try:
        cost = minimum_connection_cost(args.cables)
    except ValueError as error:
        parser.error(str(error))
    print(f'Tree minimum: {find_minimum(root)}')
    print(f'Tree sum: {sum_values(root)}')
    print(f'Minimum cable connection cost: {cost}')


if __name__ == '__main__':
    main()
