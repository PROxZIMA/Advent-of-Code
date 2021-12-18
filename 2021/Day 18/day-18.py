import os
from abc import ABC
from ast import literal_eval
from typing import Union


class Node(ABC):
    def __init__(self, level: int, parent: Union["Internal", None]) -> None:
        self.level = level
        self.parent = parent

    @property
    def is_left(self) -> Union[bool, None]:
        return None if self.parent is None else self.parent.left == self

    def add_to_leaf(self, data: int, go_left: bool) -> None:
        raise NotImplemented

    def explode(self) -> bool:
        raise NotImplemented

    def split(self) -> bool:
        raise NotImplemented

    def __str__(self) -> str:
        return f"Level: {self.level}, Parent: {self.parent}"


class Leaf(Node):
    def __init__(self, data: int, level: int, parent: "Internal") -> None:
        super().__init__(level, parent)
        self.data = data
        self.next: Union[Leaf, None] = None
        self.prev: Union[Leaf, None] = None

    @property
    def magnitude(self) -> int:
        return self.data

    def add_to_leaf(self, data: int, go_left: bool) -> None:
        self.data += data

    def get_leaf(self, go_left: bool) -> "Leaf":
        return self

    def explode(self) -> bool:
        return False

    def split(self) -> bool:
        if self.data < 10:
            return False

        left_leaf = self.prev
        right_leaf = self.next

        n = self.data
        new_internal = self.parent.add_child(
            data=[n // 2, n // 2 + n % 2],
            go_left=self.is_left,
        )

        if left_leaf:
            left_leaf.next = new_internal.left
        new_internal.left.prev = left_leaf

        new_internal.right.next = right_leaf
        if right_leaf:
            right_leaf.prev = new_internal.right

        new_internal.left.next = new_internal.right
        new_internal.right.prev = new_internal.left

        return True

    def __str__(self) -> str:
        return f"{{Data: {self.data}, Prev: {self.prev.data if self.prev else None}, Next: {self.next.data if self.next else None}}}"


class Internal(Node):
    def __init__(self, data: list, level: int, parent: Union["Internal", None]) -> None:
        super().__init__(level, parent)
        self.left, self.right = None, None
        left, right = data
        self.add_child(left, go_left=True)
        self.add_child(right, go_left=False)

        left_leaf = self.left.get_leaf(go_left=False)
        right_leaf = self.right.get_leaf(go_left=True)
        left_leaf.next = right_leaf
        right_leaf.prev = left_leaf

    @property
    def data(self) -> list:
        return [self.left.data, self.right.data]

    def child(self, go_left: bool) -> Union["Internal", Leaf]:
        return self.left if go_left else self.right

    def add_child(self, data: Union[int, list],go_left: bool) -> Union["Internal", Leaf]:
        kwargs = dict(data=data, level=self.level + 1, parent=self)
        node = Leaf(**kwargs) if isinstance(data, int) else Internal(**kwargs)
        if go_left:
            self.left = node
        else:
            self.right = node
        return node

    @property
    def magnitude(self) -> int:
        return self.left.magnitude * 3 + self.right.magnitude * 2

    def get_leaf(self, go_left: bool) -> Leaf:
        return self.child(go_left).get_leaf(go_left)

    def add_to_leaf(self, value: int, go_left: bool) -> None:
        self.child(go_left).add_to_leaf(value, go_left)

    def explode(self) -> bool:
        if self.level <= 4:
            return self.left.explode() or self.right.explode()

        left_leaf = self.left.prev
        if left_leaf:
            left_leaf.add_to_leaf(self.left.data, go_left=True)

        right_leaf = self.right.next
        if right_leaf:
            right_leaf.add_to_leaf(self.right.data, go_left=False)

        new_leaf = self.parent.add_child(0, go_left=self.is_left)

        if left_leaf:
            left_leaf.next = new_leaf
        new_leaf.prev = left_leaf

        new_leaf.next = right_leaf
        if right_leaf:
            right_leaf.prev = new_leaf

        return True

    def split(self) -> bool:
        return self.left.split() or self.right.split()

    def __str__(self) -> str:
        return f"{{Left: {self.left}, Right: {self.right}}}"


class Root(Internal):
    def __init__(self, data: list):
        super().__init__(data, level=1, parent=None)

    def connect_leaf(self, root: "Root") -> "Root":
        left_leaf = root.left.get_leaf(go_left=False)
        right_leaf = root.right.get_leaf(go_left=True)
        left_leaf.next = right_leaf
        right_leaf.prev = left_leaf

        while root.explode() or root.split():
            continue

        return root

    def __add__(self, other: "Root") -> "Root":
        return self.connect_leaf(Root([self.data, other.data]))

    def __iadd__(self, other: "Root") -> "Root":
        self.left = Internal(self.data, level=2, parent=self)
        self.right = Internal(other.data, level=2, parent=self)

        return self.connect_leaf(self)

    def __str__(self) -> str:
        return f"Left: {self.left}, Right: {self.right}"


class Genesis:
    def __iadd__(self, other: Root) -> Root:
        return other

    @property
    def magnitude(self) -> int:
        return 0


def part1(data: list[str]) -> int:
    tree = Genesis()
    for line in data:
        tree += Root(literal_eval(line))
    return tree.magnitude


def part2(data: list[str]):
    return max(
        (Root(literal_eval(num1)) + Root(literal_eval(num2))).magnitude
        for i, num1 in enumerate(data)
        for j, num2 in enumerate(data)
        if i != j
    )


def testcase():
    sailFish_numbers = open(
        os.path.join(os.path.dirname(__file__), "day-18-test.txt")
    ).read().split("\n")

    assert part1(sailFish_numbers) == 4140
    assert part2(sailFish_numbers) == 3993


if __name__ == "__main__":
    testcase()

    sailFish_numbers = open(
        os.path.join(os.path.dirname(__file__), "day-18-input.txt")
    ).read().split("\n")

    print(f"Part 1: {part1(sailFish_numbers)}")
    print(f"Part 2: {part2(sailFish_numbers)}")