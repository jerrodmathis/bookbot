def word_count(text):
    return len(text.split())

def char_count(text):
    chars = {}
    for c in text:
        lower_c = c.lower()
        if lower_c in chars:
            chars[lower_c] += 1
        else:
            chars[lower_c] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_chars(chars):
    sorted = []
    for c in chars:
        if c.isalpha():
            sorted.append({"char": c, "num": chars[c]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
