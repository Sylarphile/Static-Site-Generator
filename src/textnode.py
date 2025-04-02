from enum import Enum
from htmlnode import LeafNode
import re

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, TextType, url=None):
        self.text = text
        self.text_type = TextType
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url)

        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
        if text_node.text_type is TextType.TEXT:
            return LeafNode(None, text_node.text)
        if text_node.text_type is TextType.BOLD:
            return LeafNode("b", text_node.text)
        if text_node.text_type is TextType.ITALIC:
            return LeafNode("i", text_node.text)
        if text_node.text_type is TextType.CODE:
            return LeafNode("code", text_node.text)
        if text_node.text_type is TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        if text_node.text_type is TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        raise ValueError(f"invalid text type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError(f"invalid Markdown: {delimiter} is not closed")
            for i in range(len(split_text)):
                if split_text[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_text[i], text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            text = node.text
            image_markdown = extract_markdown_images(text)
            for image in image_markdown:
                image_alt, image_link = image[0], image[1]
                sections = text.split(f"![{image_alt}]({image_link})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                text = sections[1]
            if text:
                new_nodes.append(TextNode(text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            text = node.text
            link_markdown = extract_markdown_links(text)
            for link in link_markdown:
                link_alt, url = link[0], link[1]
                sections = text.split(f"[{link_alt}]({url})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link_alt, TextType.LINK, url))
                text = sections[1]
            if text:
                new_nodes.append(TextNode(text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def text_to_textnodes(text):

    return split_nodes_link(
        split_nodes_image(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD),
                      "_", TextType.ITALIC),
                        "`", TextType.CODE)))
