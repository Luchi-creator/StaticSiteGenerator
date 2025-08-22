from enum import Enum

class TextType(Enum):
    LINK_TYPE = "link"
    PLAIN_TYPE = "plain text"
    BOLD = "bold"
    ITALIC = "italic"

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
    
