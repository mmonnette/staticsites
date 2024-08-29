from textnode import TextNode

def main():
    test_node = TextNode("This is a text node", "bold", "https://boot.dev")
    print(test_node.__repr__())

main()