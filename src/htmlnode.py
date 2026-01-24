# HTMLNode class will represent a "node" in an HTML document tree (like a <p> tag and its contents, or an <a> tag and its contents). 
# It can be block level or inline, and is designed to only output HTML.
class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Still to be implemented")

    def props_to_html(self):

        html_attributes = ""
        
        if self.props is None or self.props == {}:
            return html_attributes
        
        else:
            for prop in self.props:
                html_attributes += f' {prop}="{self.props[prop]}"'
            return html_attributes
        
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'


#Class to generate a LeafNode - single HTML tag with no children.
class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        
        if self.value is None:
            raise ValueError
        
        if self.tag is None:
            return self.value
        
        else:
            if self.props:
                formatted_props_to_html = self.props_to_html()
                
                return f'<{self.tag}{formatted_props_to_html}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'