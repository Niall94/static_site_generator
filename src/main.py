from textnode import *
from functions import split_nodes_delimiter

def main():
    print(split_nodes_delimiter("This is text with a **bolded phrase** in the middle", "**", TextType.TEXT))

main()
