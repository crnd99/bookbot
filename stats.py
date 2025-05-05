def get_word_count(book):
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        print(f"Found {num_words} total words")

def get_char_count(book):
    letters = {}
    with open(book) as f:
        file = f.read().lower()
        for i in file:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def chars_to_sorted(dict):
    sorted = []
    for char, count in dict.items():
        if char.isalpha():
            sorted.append({"char": char, "num":count})
    
    sorted.sort(reverse=True, key=sort_on)

    return sorted



            


