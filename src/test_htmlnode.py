import unittest

from htmlnode import Tags,HTMLNode,LeafNode,ParentNode


class TestHTMLNode(unittest.TestCase):

    # def test_propstohtml_one(self):
    #     node = HTMLNode(Tags.a,None,None,{"href": "https://www.google.com","target": "_blank",})
    #     string = node.props_to_html()
    #     print(string)

    # def test_propstohtml_two(self):
    #     node = HTMLNode(Tags.a,None,None,{"target": "_blank",})
    #     string = node.props_to_html()
    #     print(string)

    # def test_propstohtml_three(self):
    #     node = HTMLNode(Tags.a,None,None,None)
    #     string = node.props_to_html()
    #     print(string)

    # def test_leaf_to_html_p(self):
    #     node = LeafNode("p", "Hello, world!")
    #     self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    #     print(node.to_html())

    # def test_leaf_to_html_two(self):
    #     node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    #     self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    #     print(node.to_html())

    # def test_leaf_to_html_three(self):
    #     node = LeafNode("div","Don t click me!", {"href": "https://www.google.com","color":"blue"})
    #     #self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    #     print(node.to_html())


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        print(parent_node.to_html())

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",)
        print(parent_node.to_html())

if __name__ == "__main__":
    unittest.main()