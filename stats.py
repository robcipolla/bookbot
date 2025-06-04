def get_num_words(text):
    return len(text.split())

def get_characters_appear(text):
    dictionary = {}
    for char in text:
        lower_char = char.lower()
        dictionary[lower_char] = dictionary.get(lower_char, 0) + 1
    return dictionary

def sort_on(dictionary):
    return dictionary["num"]

def sorted_dictionary_of_chars(chars_appear_dictionary):
    chars_list = []
    for char in chars_appear_dictionary:
        stat = {"char": char, "num": chars_appear_dictionary[char]}
        chars_list.append(stat)

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
