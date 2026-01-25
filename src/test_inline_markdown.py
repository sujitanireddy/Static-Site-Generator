import unittest
from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_delimiters_plain_text(self):
        node = TextNode("just some text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "just some text")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_simple_bold_split(self):
        node = TextNode("Normal **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Normal ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_multiple_italic_sections(self):
        node = TextNode("Hello _there_ my _friend_", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "Hello ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "there")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text, " my ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "friend")
        self.assertEqual(result[3].text_type, TextType.ITALIC)

    def test_code_delimiter(self):
        node = TextNode("Here is `code` sample", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Here is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " sample")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_non_text_nodes_unchanged(self):
        node1 = TextNode("plain", TextType.TEXT)
        node2 = TextNode("already bold", TextType.BOLD)
        result = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        # node1 may split, node2 must be passed through unchanged
        self.assertIs(result[-1], node2)
        self.assertEqual(result[-1].text_type, TextType.BOLD)

    def test_unmatched_delimiter_raises(self):
        node = TextNode("This is **broken", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

if __name__ == "__main__":
    unittest.main()