def get_word_count(text):
    words = text.split()
    return len(words)


def get_letter_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sorted_letter_count(text):
    letter_count = get_letter_count(text)
    filtered_count = {char: count for char, count in letter_count.items() if char.isalpha()}
    return sorted(filtered_count.items(), key=lambda x: x[1], reverse=True)