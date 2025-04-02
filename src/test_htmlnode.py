import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me!", {"href":"www.google.com"})
        self.assertEqual(node.to_html(), '<a href="www.google.com">Click Me!</a>')

    def test_leaf_no_tag(self):
        node = LeafNode(None, value="NO TAGS!")
        self.assertEqual(node.to_html(), "NO TAGS!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("a", "grandchild", {"href":"www.google.com"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><a href="www.google.com">grandchild</a></span></div>',
    )
        
    def test_to_html_with_grandchildren(self):
        grandchild_node2 = LeafNode("b", "grandchild2")
        grandchild_node = LeafNode("a", "grandchild", {"href":"www.google.com"})
        child_node = ParentNode("span", [grandchild_node, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><a href="www.google.com">grandchild</a><b>grandchild2</b></span></div>',
    )
        
    def test_to_html_no_tag(self):
        child_node = LeafNode("b", "no tag")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()

    def test_to_html_no_children(self):
        parent_node = ParentNode(None, [])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )