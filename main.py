from stats import get_word_count
from stats import get_char_count
from stats import chars_to_sorted



def get_book_text(input):
    with open(input) as f:
        file_contents = f.read()
        print(file_contents)


def main():
    filepath = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    get_word_count(filepath)
    print("--------- Character Count -------")
    char_counts = get_char_count(filepath)
    sorted_chars = chars_to_sorted(char_counts)
    for char in sorted_chars:
        character = char["char"]
        count = char["num"]
        print(f"{character}: {count}")

    print("============= END ===============")


main()
