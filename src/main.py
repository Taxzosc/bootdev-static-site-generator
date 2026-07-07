from textnode import TextNode, TextType
from copystatic import copy_static


def main() -> None:
    src = "./static"
    destination = "./public"
    copy_static(src, destination)
main()