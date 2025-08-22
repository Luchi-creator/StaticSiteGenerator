from enum import Enum

class Tags(Enum):
    P = "p"
    A = "a"
    H1 = "h1"
    DIV = "div"

class HTMLNode:
    def __init__(self,tags=None,value=None,children=None,props=None):
        self.tags = tags
        self.value = value
        self.children = children
        self.props = props

    def to_html():
        raise NotImplementedError("Needs implementation")
    
    def props_to_html(self):
        string = ''
        if self.props != None:
            for i in self.props:
                string += f" {i}={self.props[i]}"

        return string
    
    def __repr__(self):
        print(f"HTMLNode({self.tags.value},{self.value},{self.children},{self.props})")
