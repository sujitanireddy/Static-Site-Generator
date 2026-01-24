from htmlnode import HTMLNode

#Class to generate a LeafNode - single HTML tag with no children.
class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        
        if self.value is None:
            raise ValueError("No text to add to leaf node")
        
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