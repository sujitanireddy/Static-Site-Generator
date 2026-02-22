#Function to extract H1 heading from Markdown file

def extract_title(markdown):
    header = ''
    for c in markdown.split("\n"):
        if c.startswith("# "):
            header = c[2:].strip()
    
    if not header:
        raise Exception("H1 Header not found in markdown file")
    return header