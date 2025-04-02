from textnode import TextNode, TextType, split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode, ParentNode
from block_markdown import markdown_to_blocks

def main():
    Test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    test2 = split_nodes_delimiter([TextNode("This is a `code` delimiter test", TextType.TEXT)], "`", TextType.CODE)
    test3 = split_nodes_delimiter([TextNode("`This` is a code delimiter test", TextType.TEXT)], "`", TextType.CODE)
    test4 = split_nodes_delimiter([TextNode("`This``is` a code delimiter test", TextType.TEXT)], "`", TextType.CODE)
    test5 = split_nodes_delimiter([TextNode("this is a code delimiter `test`", TextType.TEXT)], "`", TextType.CODE)
    test6 = split_nodes_delimiter([TextNode("this is a code delimiter test", TextType.TEXT)], "`", TextType.CODE)
    test7 = markdown_to_blocks("""
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""")
    print(test7)
        
main()