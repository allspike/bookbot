from stats import get_num_words, char_count, sort_dict
import sys
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_contents = get_book_text(sys.argv[1])
        # print(file_contents)
        num_words = get_num_words(file_contents)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        num_chars = char_count(file_contents)
        print("--------- Character Count -------")
        sorted = sort_dict(num_chars)
        for entry in sorted:
            if entry["char"].isalpha():
                print(f"{entry["char"]}: {entry["num"]}")
        print("============= END ===============")
main()
