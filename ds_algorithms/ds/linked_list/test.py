import unittest

from singly_linked_list import SinglyLinkedList, Node


class TestSinglyLinkedList(unittest.TestCase):
    def test_append(self):
        ls = SinglyLinkedList()
        ls.append("a").append("b")
        self.assertEqual(2, ls.length)
        self.assertEqual("a", ls.head.value)
        self.assertEqual("b", ls.head.next.value)

    def test_prepend(self):
        ls = SinglyLinkedList()
        ls.append("b").append("c")
        ls.prepend("a")
        self.assertEqual("a", ls.head.value)

    def test_insert(self):
        ls = SinglyLinkedList()
        ls.append("a").append("b").append("d")
        ls.insert(2, "c")
        self.assertEqual("c", ls.head.next.next.value)

    def test_find(self):
        ls = SinglyLinkedList()
        ls.append("a").append("b").append("c")
        self.assertIsInstance(ls.find("c"), Node)
        self.assertIsNone(ls.find("d"))


if __name__ == "__main__":
    unittest.main()
