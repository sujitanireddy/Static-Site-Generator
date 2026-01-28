#function to create markdown strings from TextNodes
from textnode import TextNode, TextType
from extract_markdown_images_links import extract_markdown_images, extract_markdown_links

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

#split raw markdown test into TextNodes based on images
def split_nodes_image(old_nodes):
    
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        
        else:
            original_text = old_node.text
            images = extract_markdown_images(original_text)

            if not images:
                new_nodes.append(old_node)
            
            else:
                for image in images:
                    alt = image[0]
                    url = image[1]
                    markdown_chunk = f"![{alt}]({url})"
                    sections = original_text.split(markdown_chunk, 1)

                    if sections[0]:
                            new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                    original_text = sections[1]
    
                if original_text:
                        new_nodes.append(TextNode(original_text, TextType.TEXT))
    
    return new_nodes
                        
    
#split raw markdown test into TextNodes based on Links
def split_nodes_link(old_nodes):

    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        
        else:
            original_text = old_node.text
            links = extract_markdown_links(original_text)

            if not links:
                new_nodes.append(old_node)
            
            else:
                for link in links:
                    text = link[0]
                    url = link[1]
                    markdown_chunk = f"[{text}]({url})"
                    sections = original_text.split(markdown_chunk, 1)

                    if sections[0]:
                            new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                    original_text = sections[1]
    
                if original_text:
                        new_nodes.append(TextNode(original_text, TextType.TEXT))
    
    return new_nodes


def text_to_textnodes(text):

    node = [TextNode(text, TextType.TEXT)]

    bold_nodes = split_nodes_delimiter(node, '**', TextType.BOLD)
    bold_italic_nodes = split_nodes_delimiter(bold_nodes, '_', TextType.ITALIC)
    bold_italic_code_nodes = split_nodes_delimiter(bold_italic_nodes, '`', TextType.CODE)
    
    return split_nodes_link(split_nodes_image(bold_italic_code_nodes))