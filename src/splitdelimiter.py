#function to create markdown strings from TextNodes
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        
        else:

            parts = old_node.text.split(delimiter)

            if len(parts) % 2 == 0:
                raise Exception("Invalid Markdown")
    
            for i in range(len(parts)):
                part = parts[i]
                if not part:
                    continue  # skip empty strings

                if i % 2 == 0:
                    # outside delimiters
                    node = TextNode(part, TextType.TEXT)
                else:
                    # inside delimiters
                    node = TextNode(part, text_type)
                
                new_nodes.append(node)
        
    return new_nodes