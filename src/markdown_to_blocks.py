#Function to convert raw markdown to list of block strings
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result = []

    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        result.append(block)

    return result