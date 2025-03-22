from textnode import TextNode, TextType

def main():
    Test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(Test)


main()