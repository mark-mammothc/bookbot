def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    x = list_of_dict(chars_dict)
    x.sort(reverse=True, key=sort_on)
    print_report(num_words, book_path, x)

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


def get_book_text(path):
    with open(path) as f:
        return f.read()


def list_of_dict(dictionary):
    list_dict = []
    for key, value in dictionary.items():
        if key.isalpha():
            list_dict.append({"letter": key, "num":value})
    return list_dict


def sort_on(list_d):
    return list_d["num"]

def print_report(word_count, path, data):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("\n")
    for i in data:
        print(f"The '{i['letter']}' character was found : {i['num']} times")
    print("--- End report ---")

main()
