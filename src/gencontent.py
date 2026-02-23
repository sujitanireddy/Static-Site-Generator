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

    markdown_string = open(from_path).read()
    template_content = open(template_path).read()

    html_node = markdown_to_html_node(markdown_string)

    html_string = html_node.to_html()

    title = extract_title(markdown_string)

    template_content = template_content.replace('{{ Title }}', title)
    template_content = template_content.replace('{{ Content }}', html_string)

    #Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.




    



generate_page(from_path="/Users/sujitreddy/workspace/github.com/sujitanireddy/Static-Site-Generator/content/index.md", template_path="/Users/sujitreddy/workspace/github.com/sujitanireddy/Static-Site-Generator/template.html", dest_path="/Users/sujitreddy/workspace/github.com/sujitanireddy/Static-Site-Generator/public/dest/inject.txt")