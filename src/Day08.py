import itertools
import re
import math

from utils import read_input


class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


def build_graph(rows):
    # Construct all nodes
    nodes = dict()
    connections = dict()
    for row in rows:
        m = re.match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", row)
        name = m.group(1)
        nodes[name] = Node(name)
        connections[name] = (m.group(2), m.group(3))

    # Add connections
    for name, node in nodes.items():
        left, right = connections[name]
        node.left = nodes[left]
        node.right = nodes[right]

    return nodes


def steps_to_reach_destination(node, directions, dest_crit):
    steps = 0
    direction = itertools.cycle(directions)
    while not dest_crit(node):
        steps += 1
        node = node.left if next(direction) == "L" else node.right
    return steps


if __name__ == "__main__":
    # Read input and build graph
    rows = read_input("Day08-Puzzle")
    directions = rows[0]
    graph = build_graph(rows[2:])

    # Move through the graph
    steps = steps_to_reach_destination(
        graph["AAA"], directions, lambda node: node.name == "ZZZ"
    )
    print(f"Solution 1: {steps}")

    # Move through the graph again - figure out how many steps we need for each
    # start node to reach an end node. After that, it cycles, so we just need to
    # find the least common multiple of all of these numbers.
    steps_per_node = [
        steps_to_reach_destination(node, directions, lambda node: node.name[-1] == "Z")
        for node in graph.values()
        if node.name[-1] == "A"
    ]
    steps = math.lcm(*steps_per_node)
    print(f"Solution 2: {steps}")
