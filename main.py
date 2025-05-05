import sys
from stats import get_word_count
from stats import get_char_count
from stats import chars_to_sorted



def get_book_text(input):
    with open(input) as f:
        file_contents = f.read()
        print(file_contents)


def main():
    if len(sys.argv) == 2:
        print("============ BOOKBOT ============")
        print("----------- Word Count ----------")
        get_word_count(sys.argv[1])
        print("--------- Character Count -------")
        char_counts = get_char_count(sys.argv[1])
        sorted_chars = chars_to_sorted(char_counts)
        for char in sorted_chars:
            character = char["char"]
            count = char["num"]
            print(f"{character}: {count}")

        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        


main()
