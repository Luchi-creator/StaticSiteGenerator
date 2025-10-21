import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected)

    def test_bold_split(self):
        node = TextNode("This is text with a **code block** word", TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_italic_split(self):
        node = TextNode("This is text with a _code block word_", TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block word", TextType.ITALIC),
            TextNode("", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(result, expected)

    def test_odd_delimiter_raises(self):
        node = TextNode("This is text with a _code block word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

if __name__ == "__main__":
    unittest.main()