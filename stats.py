def get_num_words(book_contents):
    words = book_contents.split()
    return len(words)
def char_count(book_contents):
    counts = dict()
    for char in book_contents:
        if char.lower() not in counts:
            counts[char.lower()] = 1
        else:
            counts[char.lower()] += 1
    return counts
def sort_on(items):
    return items["num"]
def sort_dict(char_dict):
    new_list = []
    for item in char_dict:
        new_list.append({"char": item, "num": char_dict[item]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
