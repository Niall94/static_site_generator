import unittest

from htmlnode import HTMLNode

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