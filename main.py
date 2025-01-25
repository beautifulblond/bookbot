def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    #report = get_report(chars_dict) fuck this shit
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    
    
def get_num_words(text):
    words = text.split()
    return len(words)
    

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#Fucking uselesspos code fml
'''def get_report(dictionary):
    letter = ""
    count = 0
    report_str = f"The \'{letter}\' character was found {count} times"
    
    
    for i in dictionary:
        if i.isalpha():
            letter = i
            count = dictionary[i]
            report_str = f"The \'{letter}\' character was found {count} times"
            print(report_str)
    
    list_of_dicts = [{key: value} for key, value in dictionary.items()]
    
    
    
    sorted_ls_dicts = list_of_dicts.sort(key=lambda x: x, reverse=True)
    #print(sorted_ls_dicts)
    print(list_of_dicts.sort())
    return None'''

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse= True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()