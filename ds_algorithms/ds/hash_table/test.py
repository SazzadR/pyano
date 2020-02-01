import unittest

from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_set_and_get(self):
        hashtable = HashTable(5)
        hashtable.set("foo", "bar")
        self.assertEqual(hashtable.get("foo"), "bar")

    def test_keys(self):
        hashtable = HashTable(5)
        hashtable.set("foo", "bar")
        hashtable.set("lorem", "ipsum")
        self.assertEqual(sorted(hashtable.keys()), sorted(["foo", "lorem"]))


if __name__ == "__main__":
    unittest.main()
