import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<h1>", "lorum ipsum", None, {"href":"www.google.com", "target": "_blank"})
        node2 = HTMLNode("<h1>", "lorum ipsum", None, {"href":"www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_eq2(self):
        child1 = HTMLNode(tag="p", value="Some text")
        child2 = HTMLNode(tag="img", props={"src": "image.png"})
        nested_child = HTMLNode(tag="span", value="Nested content")
        child3 = HTMLNode(tag="div", children=[nested_child])
        parent_node = HTMLNode(children=[child1, child2, child3], props={"href":"www.google.com", "target": "_blank"})
        parent_node2 = HTMLNode(children=[child1, child2, child3], props={"href":"www.google.com", "target": "_blank"})
        self.assertEqual(parent_node, parent_node2)

    def test_eq_false(self):
        node = HTMLNode("<h1>", "lorum ipsum", None, {"href":"www.google.com", "target": "_blank"})
        node2 = HTMLNode("<p>", "lorum ipsum", None, {"href":"www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = HTMLNode("<h1>", "lorum ipsum", None, {"href":"www.google.com", "target": "_blank"})
        node2 = HTMLNode("<h1>", "lorum ipsum", None, {"href":"www.google.com"})
        self.assertNotEqual(node, node2)

    def test_eq_false3(self):
        child1 = HTMLNode(tag="p", value="Some text")
        child2 = HTMLNode(tag="img", props={"src": "image.png"})
        nested_child = HTMLNode(tag="span", value="Nested content")
        child3 = HTMLNode(tag="div", children=[nested_child])
        parent_node = HTMLNode(children=[child1, child2, child3], props={"href":"www.google.com", "target": "_blank"})
        parent_node2 = HTMLNode(children=[child1, child2], props={"href":"www.google.com", "target": "_blank"})
        self.assertNotEqual(parent_node, parent_node2)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        ) 
        
    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )