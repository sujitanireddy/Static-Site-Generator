import unittest
from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube",
                    TextType.LINK,
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
            new_nodes,
        )

    def test_text_to_textnodes_simple_mixed_formats(self):
        # arrange
        text = "This is **text** with an _italic_ word and a `code block`"

        # act
        result = text_to_textnodes(text)

        # assert: correct length
        assert len(result) == 6

        # assert: types
        assert result[0].text_type == TextType.TEXT
        assert result[1].text_type == TextType.BOLD
        assert result[2].text_type == TextType.TEXT
        assert result[3].text_type == TextType.ITALIC
        assert result[4].text_type == TextType.TEXT
        assert result[5].text_type == TextType.CODE

        # assert: texts
        assert result[0].text == "This is "
        assert result[1].text == "text"
        assert result[2].text == " with an "
        assert result[3].text == "italic"
        assert result[4].text == " word and a "
        assert result[5].text == "code block"

if __name__ == "__main__":
    unittest.main()