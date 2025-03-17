def count_words(text):
    num_words = text.split()
    return len(num_words)

def count_characters(text):
    letters = {}
    for t in text.lower():
        if t in letters:
            letters[t] += 1
        else:
            letters[t] = 1

    return letters

def sort_on(dict):
    return dict["count"]

def sort_letters(letters):
    letters_list = []
    for char, count in letters.items():
        letters_list.append(({"char": char, "count": count}))

    letters_list.sort(key=sort_on, reverse=True)
    return letters_list
