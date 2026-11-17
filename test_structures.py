import unittest

from CustomDataStructures.CustomArray import Array, DynamicArray
from CustomDataStructures.CustomBST import BST
from CustomDataStructures.CustomHashTable import HashTable
from CustomDataStructures.CustomLinkedList import DoublyLinkedList, SinglyLinkedList
from CustomDataStructures.SQDQ import Deque, Queue, Stack


class StructuresTest(unittest.TestCase):
    def test_fixed_array(self):
        items = Array(3)
        items.append(1)
        items.append(3)
        items.insert(1, 2)
        self.assertEqual(items.to_list(), [1, 2, 3])
        with self.assertRaises(OverflowError):
            items.append(4)
        self.assertEqual(items.delete_at(1), 2)
        self.assertEqual(items.search(3), 1)
        with self.assertRaises(IndexError):
            items.get(-1)

    def test_dynamic_array_resize(self):
        items = DynamicArray(2)
        for value in range(20):
            items.append(value)
        self.assertGreaterEqual(items.capacity, 20)
        for _ in range(18):
            items.delete_at(len(items) - 1)
        self.assertEqual(items.to_list(), [0, 1])
        self.assertEqual(items.capacity, 4)

    def test_singly_linked_list(self):
        items = SinglyLinkedList()
        items.append(2)
        items.prepend(1)
        items.append(3)
        self.assertTrue(items.delete_value(2))
        self.assertFalse(items.delete_value(8))
        self.assertEqual(items.to_list(), [1, 3])
        self.assertEqual(items.delete_last(), 3)
        self.assertEqual(items.delete_first(), 1)
        with self.assertRaises(IndexError):
            items.delete_last()

    def test_doubly_linked_list(self):
        items = DoublyLinkedList()
        for value in (2, 3, 4):
            items.append(value)
        items.prepend(1)
        self.assertTrue(items.delete_value(3))
        self.assertEqual(items.to_list_reverse(), [4, 2, 1])
        self.assertEqual(items.delete_last(), 4)
        self.assertEqual(items.delete_first(), 1)
        self.assertEqual(items.delete_last(), 2)
        self.assertIsNone(items.head)
        self.assertIsNone(items.tail)

    def test_stack(self):
        items = Stack()
        items.push("first")
        items.push("last")
        self.assertEqual(items.peek(), "last")
        self.assertEqual(items.pop(), "last")
        self.assertEqual(items.pop(), "first")
        with self.assertRaises(IndexError):
            items.pop()

    def test_queue(self):
        items = Queue()
        items.enqueue(1)
        items.enqueue(2)
        self.assertEqual(items.dequeue(), 1)
        self.assertEqual(items.peek(), 2)
        self.assertEqual(items.dequeue(), 2)
        self.assertTrue(items.is_empty())

    def test_deque(self):
        items = Deque()
        items.add_front(1)
        items.add_back(2)
        items.add_front(0)
        self.assertEqual(items.remove_back(), 2)
        self.assertEqual(items.remove_front(), 0)
        self.assertEqual(items.peek_back(), 1)
        self.assertEqual(items.to_list(), [1])

    def test_hash_table_collisions_and_resize(self):
        table = HashTable(capacity=2, max_load=1)
        table.put(0, "zero")
        table.put(2, "two")
        self.assertEqual(table.stats()["longest chain"], 2)
        table.put(2, None)
        self.assertIn(2, table)
        table.put("three", 3)
        self.assertEqual(table.resizes, 1)
        self.assertEqual(table.get(0), "zero")
        self.assertEqual(table.get("three"), 3)
        self.assertTrue(table.delete(2))
        self.assertNotIn(2, table)

    def test_bst_removal_and_traversal(self):
        tree = BST()
        for key in (5, 3, 7, 2, 4, 6, 8):
            tree.insert(key)
        self.assertFalse(tree.insert(5))
        self.assertTrue(tree.delete(2))
        self.assertTrue(tree.delete(3))
        self.assertTrue(tree.delete(5))
        self.assertFalse(tree.search(5))
        self.assertEqual(tree.inorder(), [4, 6, 7, 8])
        self.assertEqual(tree.height(), 3)
        self.assertFalse(tree.delete(10))

    def test_bst_sorted_input(self):
        tree = BST()
        for key in range(1100):
            tree.insert(key)
        self.assertEqual(tree.height(), 1100)
        self.assertEqual(tree.inorder(), list(range(1100)))


if __name__ == "__main__":
    unittest.main()
