from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

#Converts a full markdown doc to a HTMLNode 
def markdown_to_html_node(markdown):

    #Splits the markdown into blocks
    blocks = markdown_to_blocks(markdown)

    collection = []

    for block in blocks:

        if not block: #skipping empty blocks
            continue

        block_type = block_to_block_type(block) #Determines the type of block

        if block_type == BlockType.HEADING:
            block_type_heading(block, collection)

        if block_type == BlockType.PARAGRAPH:
            block_type_paragraph(block, collection)

        if block_type == BlockType.ULIST:
            block_type_unorderedlist(block, collection)
    
        if block_type == BlockType.OLIST:
            block_type_orderedlist(block, collection)

        if block_type == BlockType.QUOTE:
            block_type_quote(block, collection)

        if block_type == BlockType.CODE:
            block_type_code(block, collection)

    return ParentNode(children=collection, tag="div")


def block_type_heading(block, collection):
    for i, char in enumerate(block):
        if char == ' ':
            break
    heading_size = len(block[:i])
    heading_text = block[i:].strip()
    collection.append(ParentNode(children=text_to_children(heading_text), tag=f"h{heading_size}"))


def block_type_paragraph(block, collection):
    block_to_line = " ".join(block.split("\n"))
    collection.append(ParentNode(children=text_to_children(block_to_line), tag="p"))


def block_type_unorderedlist(block, collection):
    li_nodes = []
    for line in block.split("\n"):
        line_text = line[1:].strip()
        li_nodes.append(ParentNode(children=text_to_children(line_text), tag="li"))
    collection.append(ParentNode(children=li_nodes, tag="ul"))


def block_type_orderedlist(block, collection):
    li_nodes = []
    for line in block.split("\n"):
        for i, char in enumerate(line):
            if char == ' ':
                break
        line_text = line[i:].strip()
        li_nodes.append(ParentNode(children=text_to_children(line_text), tag="li"))
    collection.append(ParentNode(children=li_nodes, tag="ol"))


def block_type_quote(block, collection):
    quote_text = " ".join([quote[1:].strip() for quote in block.split("\n")])
    collection.append(ParentNode(children=text_to_children(quote_text), tag="blockquote"))


def block_type_code(block, collection):
    code_node = ParentNode(children=[text_node_to_html_node(TextNode(text=block[4:-3],text_type=TextType.TEXT))], tag="code")
    collection.append(ParentNode(children=[code_node], tag="pre"))


#Converts raw text to TextNodes
def text_to_children(text):

    text_nodes = text_to_textnodes(text)

    children = []
    
    for text in text_nodes:
        children.append(text_node_to_html_node(text))

    return children