from enum import Enum
from leafnode import LeafNode

#Enum class for all the different types of inline text (text nodes).
class TextType(Enum):
    TEXT = "text"
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

#TextNode class" represents the various types of inline text that can exist in HTML and Markdown.
class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
            
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

#Function to convert TextNode to an HTMLNode
def text_node_to_html_node(text_node):

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, value=text_node.text)
    
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag='b', value=text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag='i', value=text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag='code', value=text_node.text)
    
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag='a', value=text_node.text, props={"href" : text_node.url})
    
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag='img', value='', props={"src": text_node.url, "alt": text_node.text})
    
    else:
        raise Exception("TextNode does not match any type")

    