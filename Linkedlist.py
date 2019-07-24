from typing import Optional


class Node(object):
    data: int
    next: "Node"

    def __init__(self, data: Optional[int] = None, next: Optional["Node"] = None):
        self.data = data
        self.next = next


class LinkedList(object):
    head: Optional[Node]
    tail: Optional[Node]
    size: int

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self) -> int:
        return self.size

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def insert(self, data: int, position: int)->bool:
        if position>self.size:
            return False
        else:
            now: Node = self.head
            for i in position-1:
                now = now.next
            insert: Node = Node(data)
            afterinsert: Node = now.next
            insert.next = afterinsert
            now.next = insert
            return True
    def delete(self, position: int)->bool:
        if position > self.size:
            return False
        else:
            now: Node = self.head
            for i in position-1:
                now = now.next

        return 0
