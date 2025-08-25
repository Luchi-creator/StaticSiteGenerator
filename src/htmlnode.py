from enum import Enum

class Tags(Enum):
    p = "p"
    a = "a"
    h1 = "h1"
    div = "div"

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Needs implementation")
    
    def props_to_html(self):
        string = ''
        if self.props != None:
            for i in self.props:
                string += f' {i}="{self.props[i]}"'

        return string
    
    def __repr__(self):
        return (f"HTMLNode({self.tag},{self.value},{self.children},{self.props})")


class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value == None:
            raise ValueError("The value property is none or empty")
        elif self.tag == None:
            return self.value
        else:
            my_props = self.props_to_html()
            return f"<{self.tag}{my_props}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag field is not assigned")
        elif self.children == None:
            raise ValueError("The children property is not assigned")
        else:
            my_string = ''
            for i in self.children:
                my_string += i.to_html()

            return f"<{self.tag}>{my_string}</{self.tag}>"   