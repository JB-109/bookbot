from stats import counted_char, descending_order, sorted_list, splited_string, get_book_text, print_def
import sys
if len(sys.argv) == 2:
    file_path = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main(file_path):
    single_string = get_book_text(file_path)
    total_strings = splited_string(single_string)
    txt_call = print_def(file_path, single_string, total_strings)
    
main(file_path)