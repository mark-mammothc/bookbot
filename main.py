import sys
from sys import argv
from stats import count_words, count_characters, sort_letters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        book_content = f.read()
    return book_content

def main():
    text = get_book_text(sys.argv[1])
    count = count_words(text)
    print(f"{count} words found in the document")
    letters = count_characters(text)
    print(letters)
    x = sort_letters(letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in x:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
    print(len(sys.argv))

if __name__ == '__main__':
    main()