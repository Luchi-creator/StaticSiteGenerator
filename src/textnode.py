from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = None
    BOLD = 'b'
    ITALIC = 'i'
    CODE = 'code'
    LINK = 'a'
    IMAGE = 'img'

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,textnode_two):
        if self.text == textnode_two.text and self.text_type == textnode_two.text_type and self.url == textnode_two.url:
            return True
        else:
            return False

    def __repr__(self):
        print(f"TextNode({self.text},{self.text_type.value},{self.url})")
    
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Not a valid text_type")
    else:
        if text_node.text_type == TextType.LINK:
            my_dict = {"href":text_node.url}
            return LeafNode(text_node.text_type.value,text_node.text,my_dict)
        elif text_node.text_type == TextType.IMAGE:
            my_dict = {"src":text_node.url,"alt":text_node.text}
            return LeafNode(text_node.text_type.value,"",my_dict)
        else:
            return LeafNode(text_node.text_type.value,text_node.text,None)
        