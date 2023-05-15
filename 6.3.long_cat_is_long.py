
def count_words(text):
    """
    This function counts the number of words in a given text and returns a
    dictionary with the word as key and its length as value.
    """
    new_text = ''.join(c for c in text if c.isalpha() or c.isspace())
    words = {word: len(word) for word in new_text.lower().split()}
    return words


def main():
    text = input("please enter some text: ")
    print(count_words(text))
    return 0


if __name__ == '__main__':
    main()