from textnode import TextNode, TextType

def split_nodes_delimiter(
        old_nodes: list[TextNode],
        delimiter: str,
        text_type: TextType) -> list[TextNode]:
    new_text = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_text.extend(node.text)