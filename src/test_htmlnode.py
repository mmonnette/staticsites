import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("p", "this is the text in the paragraph", None, {"href": "https://www.google.com", "target": "_blank"}
        )
        desired = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), desired)

    def test_repr(self):
        node = HTMLNode("p", "this is the text in the paragraph", None, {"href": "https://www.google.com", "target": "_blank"}
        )
        desired = "tag: p\nvalue: this is the text in the paragraph\nchildren: None\nprops: {'href': 'https://www.google.com', 'target': '_blank'}"
        self.assertEqual(node.__repr__(), desired)

if __name__ == "__main__":
    unittest.main()