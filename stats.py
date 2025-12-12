def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)
    

def count_unique_characters(text):
    unique_characters = {}
    longstring = list(text.lower())
    for i in longstring:
        if i not in unique_characters:
            unique_characters[i] = 1
        else:
            unique_characters[i] += 1
    return unique_characters

def sort_characters(char_counts):
    old_list = list(char_counts.items())
    new_list = []
    for character, num in old_list:
        new_dict = {"char": character, "num": num}
        new_list.append(new_dict)

    def sort_on(items):
        return items["num"]
    new_list.sort(reverse=True, key=sort_on)
    return new_list

