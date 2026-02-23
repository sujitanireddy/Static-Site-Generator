import os

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


def generate_page(from_path, template_path, dest_path):

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

    directory = os.path.dirname(dest_path)
    
    # Create the directory and any missing parent directories
    if directory != "":
        os.makedirs(directory, exist_ok=True)
    
    # Open the file and write the content
    with open(dest_path, "w") as f:
        f.write(template_content)