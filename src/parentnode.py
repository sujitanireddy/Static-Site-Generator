from htmlnode import HTMLNode

#Class to generate a ParentNode - Any HTML node that's not "leaf" node (i.e. it has children) is a "parent" node.
class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):

        if self.tag is None:
            raise ValueError("No tag to add to parent node")

        if not self.children:
            raise ValueError("children are missing")

        child_accumulator = ''

        for child in self.children:

            child_accumulator += child.to_html()
        
        if self.props:
            formatted_props_to_html = self.props_to_html()
            return f'<{self.tag}{formatted_props_to_html}>{child_accumulator}</{self.tag}>'
        else:
            return f'<{self.tag}>{child_accumulator}</{self.tag}>'
    
    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'