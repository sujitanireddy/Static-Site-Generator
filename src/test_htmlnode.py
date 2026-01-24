#Unit tests to validate htmlnodes
import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode(tag='p', value='Testing of HTML nodes', props=None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_empty_dict(self):
        node = HTMLNode(tag='p', value='Testing of HTML nodes', props={})
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html(self):
        node = HTMLNode(tag='p', value='Testing of HTML nodes', props={"href": "www.youtube.com", "title": "davinci resolve"})
        self.assertEqual(node.props_to_html(), f' href="www.youtube.com" title="davinci resolve"')


if __name__ == "__main__":
    unittest.main()