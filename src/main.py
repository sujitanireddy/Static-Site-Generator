from textnode import TextNode, TextType

def main():

    test_object = TextNode("testing", TextType.CODE, "www.test.com")
    print(test_object)

if __name__ == "__main__":
    main()