import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode('abcd', TextType.ITALIC)
        node4 = TextNode('abcd', TextType.ITALIC, None)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertEqual(node3, node4)


if __name__ == "__main__":
    unittest.main()