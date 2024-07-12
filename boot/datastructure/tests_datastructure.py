import unittest

from data_structures import Stack, last_item


class TestsDataStructure(unittest.TestCase):
    def test_last_item(self):
        inventory = [
            "Short sword",
            "Bread",
            "Healing potion",
            "Leather scraps",
            "Chainmail Armor",
        ]
        self.assertEqual(last_item(inventory), "Chainmail Armor")

    def test_stack_add(self):
        stack = Stack()
        stack.push("Hello")
        stack.push("World")
        self.assertEqual(stack.peek(), "World")
