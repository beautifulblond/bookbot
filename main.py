def main():
    '''with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)'''
    word_count()
    char_count()

def word_count():
    word_count = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    for word in words:
        word_count += 1
    print(f"There are {word_count} words in frankenstein.txt!")

def char_count():
    char_ls = []
    char_dict = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    file_contents = file_contents.lower()
    for i in file_contents:
        if i not in char_dict:
            char_dict[i] = 1
        elif i in char_dict:
            char_dict[i] += 1
    print(char_dict)
    
main()