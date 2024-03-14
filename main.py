
import operator

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)
    
lowered_file_contents = file_contents.lower()  
#alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    characters_dict = count_characters(text)
    num_words = count_words()
    chars_sorted_list = chars_dict_to_sorted_list(characters_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
        
    print("--- End report ---")
    
    
def count_words():
    num_words = 0
    words = file_contents.split()
    for word in words:
        num_words += 1
    return num_words

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

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
