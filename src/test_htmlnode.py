import unittest

from htmlnode import Tags,HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_propstohtml_one(self):
        node = HTMLNode(Tags.A,None,None,{"href": "https://www.google.com","target": "_blank",})
        string = node.props_to_html()
        print(string)

    def test_propstohtml_two(self):
        node = HTMLNode(Tags.A,None,None,{"target": "_blank",})
        string = node.props_to_html()
        print(string)

    def test_propstohtml_three(self):
        node = HTMLNode(Tags.A,None,None,None)
        string = node.props_to_html()
        print(string)

if __name__ == "__main__":
    unittest.main()