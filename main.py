def main():
    '''with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)'''
    word_count()

def word_count():
    word_count = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    for word in words:
        word_count += 1
    print(f"There are {word_count} words in frankenstein.txt!")
    
main()