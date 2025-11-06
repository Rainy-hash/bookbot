def word_count(book_contents):
    words = book_contents.split()
    print(f"Found {len(words)} total words")

def char_count(book_contents):
    char = book_contents.lower()
    char_dict = {}

    for char in char:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sorted_dicts(book_contents):
    char_dict = char_count(book_contents)
    sort_list = []

    for i in char_dict:
        sort_list.append({"char": i, "num": char_dict[i]})

    def sort_items(items):
        return items["num"]
    
    sort_list.sort(key=sort_items, reverse=True)
    for item in sort_list:
        print(f"{item['char']}: {item['num']}")