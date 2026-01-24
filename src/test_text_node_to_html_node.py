#Unit tests to validate text node to html node function
import unittest

from textnode import TextNode, TextType, text_node_to_html_node

def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

def test_italic(self):
    node = TextNode("slanted", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, 'i')
    self.assertEqual(html_node.value, "slanted")

def test_link(self):
    node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, 'a')
    self.assertEqual(html_node.value, "Boot.dev")

if __name__ == "__main__":
    unittest.main()