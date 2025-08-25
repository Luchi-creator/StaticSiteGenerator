import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    # def test_eq(self):
    #     node = TextNode("This is a text node", TextType.BOLD)
    #     node2 = TextNode("This is a text node", TextType.BOLD)
    #     print(self.assertEqual(node, node2))
    #     node.__repr__()
    #     node2.__repr__()


    # def test_property_link(self):
    #     node = TextNode("da",TextType.ITALIC)
    #     node2 = TextNode("da",TextType.ITALIC,"www.cv.com")
    #     print(self.assertNotEqual(node,node2))

    # def test_property_text_type(self):
    #     node = TextNode("da",TextType.BOLD)
    #     node2 = TextNode("da",TextType.ITALIC,None)
    #     print(self.assertNotEqual(node, node2))

    # def test_property_text(self):
    #     node = TextNode("dadada",TextType.BOLD)
    #     node2 = TextNode("da",TextType.ITALIC,None)
    #     print(self.assertNotEqual(node, node2))

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        print(html_node.to_html())

    def test_text_one(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.to_html(), "<b>This is a text node</b>")
        print(html_node.to_html())

    def test_text_three(self):
        node = TextNode("This is a link node", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.to_html(), '<a href="www.google.com">This is a link node</a>')
        print(html_node.to_html())

    def test_text_four(self):
        node = TextNode("This is a image node", TextType.IMAGE, "./magicfolder")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.to_html(), '<img src="./magicfolder" alt="This is a image node"></img>')
        print(html_node.to_html())

if __name__ == "__main__":
    unittest.main()