from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from splitdelimiter import text_to_textnodes


#Converts a full markdown doc to a HTMLNode 
def markdown_to_html_node(markdown):

    #Splits the markdown into blocks
    blocks = markdown_to_blocks(markdown)

    collection = []

    for block in blocks:

        block_type = block_to_block_type(block) #Determines the type of block

        if block_type == BlockType.HEADING:
            heading_size = 0
            heading_text = ""
            for i, char in enumerate(block):
                if char == ' ':
                    break
            heading_size = len(block[:i])
            heading_text = block[i:].strip()
            collection.append(ParentNode(children=text_to_children(heading_text), tag=f"h{heading_size}"))

        if block_type == BlockType.PARAGRAPH:
            block_to_line = " ".join(block.split("\n"))
            collection.append(ParentNode(children=text_to_children(block_to_line), tag="p"))

        if block_type == BlockType.ULIST:
            li_nodes = []
            for line in block.split("\n"):
                line_text = line[1:].strip()
                li_nodes.append(ParentNode(children=text_to_children(line_text), tag="li"))
            collection.append(ParentNode(children=li_nodes, tag="ul"))
        
        if block_type == BlockType.OLIST:
            li_nodes = []
            for line in block.split("\n"):
                for i, char in enumerate(line):
                    if char == ' ':
                        break
                line_text = line[i:].strip()
                li_nodes.append(ParentNode(children=text_to_children(line_text), tag="li"))
            collection.append(ParentNode(children=li_nodes, tag="ol"))

        if block_type == BlockType.QUOTE:
            quote_text = " ".join([quote[1:] for quote in block.split("\n")])
            collection.append(ParentNode(children=text_to_children(quote_text), tag="blockquote"))

        if block_type == BlockType.CODE:
            code_node = ParentNode(children=[text_node_to_html_node(TextNode(text=block[3:-3],text_type=TextType.TEXT))], tag="code")
            collection.append(ParentNode(children=[code_node], tag="pre"))
        
    return ParentNode(children=collection, tag="div")

        
#Converts raw text to TextNodes
def text_to_children(text):

    text_nodes = text_to_textnodes(text)

    children = []
    
    for text in text_nodes:
        children.append(text_node_to_html_node(text))

    return children


#testing
markdown_to_html_node(markdown="""
- This is a simple item
- This has **bold** text
- This has _italics_ and `code`

1. First step: Gather ingredients
2. Second step: Boil the water
3. Third step: Add the **Phoenix feather**

```
function test() {
  console.log("notice the blank line before this function?");
}
```
""")