from textnode import TextNode
from htmlnode import *

def main():
    test_node = LeafNode("p", "This is a paragraph of text.")
    print(test_node.to_html())

main()