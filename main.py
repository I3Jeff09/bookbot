import sys
from stats import sort_characters, count_unique_characters, get_book_text, count_words

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    path = sys.argv[1]
    text = get_book_text(path)
    char_counts = count_unique_characters(text)
    sort_chars = sort_characters(char_counts)
    num_words = count_words(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sort_chars:
        ch = i["char"]
        num = i["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")

main()