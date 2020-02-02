import json


class Node(object):
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        response = []
        current = self.head
        while current:
            response.append({
                "value": current.value,
                "previous": current.previous.value if current.previous else None,
                "next": current.next.value if current.next else None
            })
            current = current.next
        return json.dumps(response)

    def _remove(self, node):
        del node
        self.length -= 1

    def prepend(self, value):
        # O(1)
        node = Node(value)
        node.next = self.head
        temp = self.head
        temp.previous = node
        self.head = node
        self.length += 1

    def append(self, value):
        # O(1)
        self.length += 1
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return self
        temp = self.tail
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.tail.previous = temp
        return self

    def insert(self, index, value):
        # O(n)
        if index >= self.length:
            raise IndexError(f"Please enter a valid index between [0..{self.length - 1}]")
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        new_node = Node(value)
        new_node.next = temp.next
        new_node.previous = temp
        temp.next = new_node
        self.length += 1
        return self

    def find(self, value):
        # O(n)
        current = self.head
        while current.next:
            current = current.next
            if current.value == value:
                return current
        return None

    def remove_head(self):
        # O(1)
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        self.head.previous = None
        self._remove(temp)
        return self

    def remove_tail(self):
        # O(n)
        prev = self.head
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self._remove(temp)

    def remove(self, index):
        # O(n)
        if index <= 0 or index >= (self.length - 1):
            raise IndexError(f"Please enter a valid index between [1..{self.length - 2}]")
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        to_delete = temp.next
        temp.next = to_delete.next
        temp.next.previous = to_delete.previous
        self._remove(to_delete)
