import os
import pathlib
from markdown_to_html import markdown_to_html_node

#Function to extract H1 heading from Markdown file
def extract_title(markdown):
    header = ''
    for c in markdown.split("\n"):
        if c.startswith("# "):
            header = c[2:].strip()
    
    if not header:
        raise Exception("H1 Header not found in markdown file")
    return header

#Function to generate a page
def generate_page(from_path, template_path, dest_path, basepath):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        markdown_string = f.read()

    with open(template_path, 'r') as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_string)

    html_string = html_node.to_html()

    title = extract_title(markdown_string)

    template_content = template_content.replace('{{ Title }}', title)
    template_content = template_content.replace('{{ Content }}', html_string)
    template_content = template_content.replace('href="/', f'href="{basepath}')
    template_content = template_content.replace('src="/', f'src="{basepath}')

    directory = os.path.dirname(dest_path)
    
    # Create the directory and any missing parent directories
    if directory != "":
        os.makedirs(directory, exist_ok=True)
    
    # Open the file and write the content
    with open(dest_path, "w") as f:
        f.write(template_content)

#Funtion to recursivley generate a page
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    root_dir_contents = os.listdir(dir_path_content)

    for item in root_dir_contents:
        item_path = os.path.join(dir_path_content, item)
        
        if os.path.isdir(item_path):
            generate_pages_recursive(dir_path_content=item_path, template_path=template_path, dest_dir_path=os.path.join(dest_dir_path, item))
        
        elif os.path.isfile(item_path):
            if item_path.endswith(".md"):
                new_filename = pathlib.Path(item).with_suffix(".html")
                generate_page(from_path=item_path, template_path=template_path, dest_path=os.path.join(dest_dir_path, new_filename))
            
            