def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    block_list = []
    for text in split_markdown:
        if text == "":
            continue
        block_list.append(text.strip())
    return block_list