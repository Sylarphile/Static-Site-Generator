def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block == "":
            continue
        new_block = block.strip()
        new_blocks.append(new_block)

    return new_blocks
    
