from stats import counted_char, descending_order, sorted_list, splited_string, get_book_text
import sys
if len(sys.argv) == 2:
    file_path = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main(file_path):
    single_string = get_book_text(file_path)
    total_strings = splited_string(single_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {total_strings} total words")
    print("--------- Character Count -------")
    descending_order(single_string)
    print("============= END ===============")

main(file_path)