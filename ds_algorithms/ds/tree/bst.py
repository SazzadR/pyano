import json


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        response = {
            "value": self.value,
            "left": self.left.value if self.left else None,
            "right": self.right.value if self.right else None
        }
        return json.dumps(response)


class BinarySearchTree(object):
    def __init__(self):
        self._root = None

    def _traverse(self, node):
        tree = {"value": node.value}
        tree["left"] = self._traverse(node.left) if node.left else None
        tree["right"] = self._traverse(node.right) if node.right else None
        return tree

    def get_root(self):
        return self._root

    def traverse(self):
        root = self._root
        response = self._traverse(root)
        return response

    def insert(self, value):
        node = Node(value=value)
        if self._root is None:
            self._root = node
            return self
        else:
            current_node = self._root
            while True:
                if current_node.value > node.value:
                    if current_node.left is None:
                        current_node.left = node
                        return self
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node
                        return self
                    current_node = current_node.right

    def remove(self, value):
        # empty tree
        # value is in the root node

        parent = None
        node = self._root

        while node and node.value != value:
            parent = node
            if value < node.value:
                node = node.left
            else:
                node = node.right

        if node is None or node.value != value:
            # Case 1: data not found
            return False
        elif node.left is None and node.right is None:
            # Case 2: remove-node has no children
            if value < parent.value:
                parent.left = None
            else:
                parent.right = None
            return True
        elif node.left and node.right is None:
            # Case 3: remove-node has left child only
            if value < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left
        elif node.right and node.left is None:
            # Case 4: remove-node has right child only
            if value < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right

    def search(self, value):
        def _search(current_node_nested, value_nested):
            if current_node_nested.value == value_nested:
                return current_node_nested
            elif current_node_nested.value > value_nested and current_node_nested.left is not None:
                return _search(current_node_nested.left, value_nested)
            elif current_node_nested.value < value_nested and current_node_nested.right is not None:
                return _search(current_node_nested.right, value_nested)
            else:
                return None

        current = self._root
        return _search(current, value)


if __name__ == "__main__":
    # # Case 2: remove-node has no children
    # bst = BinarySearchTree()
    # bst.insert(41).insert(20).insert(65).insert(11).insert(29).insert(50).insert(70)
    # bst.remove(11)

    # # Case 3: remove-node has left child only
    # bst = BinarySearchTree()
    # bst.insert(41).insert(20).insert(11).insert(65).insert(50).insert(70)
    # bst.remove(20)

    # Case 4: remove-node has right child only
    bst = BinarySearchTree()
    bst.insert(41).insert(20).insert(15).insert(25).insert(65).insert(75)
    bst.remove(65)

    import json
    print(json.dumps(bst.traverse()))
