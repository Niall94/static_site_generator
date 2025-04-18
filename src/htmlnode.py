class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        att_str = ""
        if self.props != None:
            for key in self.props:
                att_str += f' {key}="{self.props[key]}"'
            return att_str
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value added")
        elif self.tag == None:
            return self.value
        elif self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invlaid HTML: no tag")
        elif self.children == None:
            raise ValueError("Invalid HTML: no children")
        else:
            result = ""
            for child in self.children:
                result += child.to_html()
            return f"<{self.tag}>{result}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, Children: {self.children}, {self.props})"