import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(props={
        "href": "https://www.google.com",
        "target": "_blank",
        })

        self.assertEqual(node1.props_to_html(),  ' href="https://www.google.com" target="_blank"')

    def test_props_to_html2(self):
        node1 = HTMLNode(props={
        "href": "https://www.boot.dev",
        "target": "_blank",
        "color": "cyan"
        })

        self.assertEqual(node1.props_to_html(),  ' href="https://www.boot.dev" target="_blank" color="cyan"')

    def test_props_to_html3(self):
        node1 = HTMLNode(props={
        "href": "https://www.amazon.co.uk",
        "target": "_blank",
        "color": "red"
        })

        self.assertEqual(node1.props_to_html(),  ' href="https://www.amazon.co.uk" target="_blank" color="red"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "Click me!")
