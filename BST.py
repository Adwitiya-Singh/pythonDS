from typing import Optional


class Node(object):
    left: "Node"
    right: "Node"
    data: int

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BST(object):
    root: Optional[Node]
    size: int

    def __init__(self):
        self.root = None
        self.size = 0

    def display(self):
        self.__display(self.root)
        print("*************************")

    def __display(self, node: Node):
        if node is None:
            print("NULL => NULL <= NULL")
            return

        if node.left is not None:
            print(str(node.left.data) + " => ", end="")
        else:
            print("NULL => ", end="")

        print(str(node.data), end="")

        if node.right is not None:
            print(" <= " + str(node.right.data), end="")
        else:
            print(" <= NULL", end="")

        print()

        if node.left is not None:
            self.__display(node.left)

        if node.right is not None:
            self.__display(node.right)

    def insert(self, data: int):
        self.root = self.__insert(self.root, data)
        self.size += 1

    def __insert(self, node: Node, data: int) -> Node:
        if node is None:
            return Node(data, None, None)

        if data < node.data:
            node.left = self.__insert(node.left, data)
        else:
            node.right = self.__insert(node.right, data)
        return node

    def remove(self, data: int):
        self.root = self.__remove(self.root, data)

    def __remove(self, node: Node, data: int) -> Optional[Node]:
        if node is None:
            return node
        if data < node.data:
            node.left = self.__remove(node.left, data)
        elif data > node.data:
            node.right = self.__remove(node.right, data)
        else:
            if node.left is None:
                self.size -= 1
                return node.right
            elif node.right is None:
                self.size -= 1
                return node.left
            else:
                node.data = self.min_right(node).data
                node.right = self.__remove(node.right, node.data)
        return node

    def min_right(self, node: Optional[Node]) -> Optional[Node]:
        now: Node = node.right
        if now is None:
            return None
        while now.left is not None:
            now = now.left
        return now





