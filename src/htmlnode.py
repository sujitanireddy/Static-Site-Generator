# HTMLNode class will represent a "node" in an HTML document tree (like a <p> tag and its contents, or an <a> tag and its contents). 
class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not Implemented for HTMLNode base class")

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
        

        

        
