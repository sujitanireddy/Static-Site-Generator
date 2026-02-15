from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from parentnode import ParentNode


#Converts a full markdown doc to a HTMLNode 
def markdown_to_html_node(markdown):

    #Splits the markdown into blocks
    blocks = markdown_to_blocks(markdown)

    collection = []

    for block in blocks:

        block_type = block_to_block_type(block) #Determines the type of block

        print(block_type)

        if block_type == BlockType.PARAGRAPH:
            block_to_line = ""
            for line in block.split("\n"):
                block_to_line += f" {line}".strip()
            collection.append(ParentNode(children=text_to_children(block_to_line), tag="p"))

            
        if block_type == BlockType.HEADING:
            heading_size = 0
            heading_text = ""
            for i, char in enumerate(block):
                if char == ' ':
                    break
            heading_size = len(block[:i])
            heading_text = block[i:].strip()
            collection.append(ParentNode(children=text_to_children(heading_text), tag=f"h{heading_size}"))

        




        

        
#Converts text to TextNodes
def text_to_children(text):
    
    pass #placeholder







#testing
markdown_to_html_node(markdown="""
This is **bolded** paragraph
text in a p
tag here

### This is a #heading

This is another paragraph with _italic_ text and `code` here

""")