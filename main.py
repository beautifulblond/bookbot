
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)
    
lowered_file_contents = file_contents.lower()   
#alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(count_words())
    characters_dict = count_characters(text)
    print(characters_dict)
    
def count_words():
    num_words = 0
    words = file_contents.split()
    for word in words:
        num_words += 1
    count_words_string = (f"there are {num_words} words")
    return count_words_string

def count_characters(characters):
    count_characters_dict = {}
    characters_list = []
    for c in lowered_file_contents:
        if c in count_characters_dict:
            count_characters_dict[c] += 1
        else:
            count_characters_dict[c] = 1
    return(count_characters_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
