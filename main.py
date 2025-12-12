import sys
from stats import sorted_letter_count
from stats import get_word_count

def get_book_text(PATH):
    with open(PATH) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print("Found", get_word_count(get_book_text(book_path)), "total words")
    print("--------- Character Count -------")
    for item in sorted_letter_count(get_book_text(book_path)):
        print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()