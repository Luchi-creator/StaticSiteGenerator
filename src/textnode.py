from enum import Enum
from htmlnode import LeafNode
import re

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
        print(f"TextNode({self.text},{self.text_type},{self.url})")
    
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
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_node = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
        else:
            count = 0
            for char in node.text:
                if char == delimiter:
                    count += 1
            if count%2 != 0:
                raise Exception("Matching delimiter was not found")
            else:
                new_text = node.text.split(delimiter)
                for i in range(len(new_text)):
                    if i % 2 == 0:
                        new_node.append(TextNode(new_text[i],TextType.TEXT,None))
                    else:
                        new_node.append(TextNode(new_text[i],text_type,None))
    return new_node

def extract_markdown_images(text):
    matches = re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)',text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)',text)
    return matches