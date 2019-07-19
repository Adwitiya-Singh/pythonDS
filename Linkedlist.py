from typing import Optional


class Node(object):
    def __init__(self, data: int = None, next: Optional["Node"] = None):
        self.data = data
        self.next = next

    def get(self):
        return self.data

    def set(self, data: int):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next: Optional["Node"]):
        self.next = next


class Linkedlist(object):
    def __init__(self,head: Node):
        self.head = head
        self.size = 0

    def insert(self, data: int, position: int)->bool:
        if position>self.size:
            return False
        else:
            now: Node = self.head
            for i in position:
                now = now.next
            insert: Node = Node(data)
            afterinsert: Node = now.next
            insert.next = afterinsert
            now.next = insert
            return True
    def delete(self):
        return 0
