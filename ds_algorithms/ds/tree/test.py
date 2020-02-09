import unittest

from bst import BinarySearchTree, Node


class TestBinarySearchTree(unittest.TestCase):
    def test_root(self):
        bst = BinarySearchTree()
        bst.insert(41)
        bst.insert(20)
        bst.insert(65)

        self.assertEqual(41, bst.get_root().value)

    def test_left_right_distribution(self):
        bst = BinarySearchTree()
        bst.insert(41).insert(20).insert(65).insert(11).insert(29).insert(50).insert(70)

        expected_left_most_values = [41, 20, 11]
        expected_right_most_values = [41, 65, 70]
        self.assertEqual(
            [bst.get_root().value, bst.get_root().left.value, bst.get_root().left.left.value],
            expected_left_most_values
        )
        self.assertEqual(
            [bst.get_root().value, bst.get_root().right.value, bst.get_root().right.right.value],
            expected_right_most_values
        )

    def test_traverse(self):
        bst = BinarySearchTree()
        bst.insert(41).insert(20).insert(65).insert(11).insert(29).insert(50).insert(70)

        self.assertEqual(bst.traverse(), {
            "value": 41,
            "left": {
                "value": 20,
                "left": {
                    "value": 11,
                    "left": None,
                    "right": None
                },
                "right": {
                    "value": 29,
                    "left": None,
                    "right": None
                }
            },
            "right": {
                "value": 65,
                "left": {
                    "value": 50,
                    "left": None,
                    "right": None
                },
                "right": {
                    "value": 70,
                    "left": None,
                    "right": None
                }
            }
        })

    def test_search(self):
        bst = BinarySearchTree()
        bst.insert(41).insert(20).insert(65).insert(11).insert(29).insert(50).insert(70)

        self.assertEqual(bst.search(50).value, 50)
        self.assertEqual(bst.search(50).left, None)
        self.assertEqual(bst.search(50).right, None)

        self.assertEqual(bst.search(20).value, 20)
        self.assertEqual(bst.search(20).left.value, 11)
        self.assertEqual(bst.search(20).right.value, 29)

        self.assertEqual(bst.search(100), None)


if __name__ == "__main__":
    unittest.main()
