import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        print(self.assertEqual(node, node2))
        node.__repr__()
        node2.__repr__()


    def test_property_link(self):
        node = TextNode("da",TextType.ITALIC)
        node2 = TextNode("da",TextType.ITALIC,"www.cv.com")
        print(self.assertNotEqual(node,node2))

    def test_property_text_type(self):
        node = TextNode("da",TextType.BOLD)
        node2 = TextNode("da",TextType.ITALIC,None)
        print(self.assertNotEqual(node, node2))

    def test_property_text(self):
        node = TextNode("dadada",TextType.BOLD)
        node2 = TextNode("da",TextType.ITALIC,None)
        print(self.assertNotEqual(node, node2))
    
if __name__ == "__main__":
    unittest.main()