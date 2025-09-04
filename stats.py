def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item):
    return item["num"]

def get_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        if char.isalpha():
            sorted_list.append({"char": char, "num": chars_dict[char]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list