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
        

        

        
