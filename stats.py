def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def splited_string(single_string):
    total_words = single_string.split()
    return len(total_words)


def counted_char(single_string):
    final_dict = {}
    for alpha in single_string:
        lowered_alpha = alpha.lower()
        if lowered_alpha in final_dict:
            final_dict[lowered_alpha] += 1
        else:
            final_dict[lowered_alpha] = 1    
    return final_dict


def sorted_list(single_string):
    final_list = []
    existing_dict = counted_char(single_string)
    for char in existing_dict:
        temp_dict = {}
        temp_dict["char"] = char
        temp_dict["num"] = existing_dict[char]
        final_list.append(temp_dict)
        final_list.sort(key=lambda x: x["num"], reverse=True)
    return final_list

def descending_order(single_string):
    existing_list = sorted_list(single_string)
    for each in existing_list:
        alpha_check = each["char"].isalpha() 
        if alpha_check:
            print(f"{each["char"]}: {each["num"]}")
        else:
            continue
    return 

def print_def(file_path, single_string, total_strings):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {total_strings} total words")
    print("--------- Character Count -------")
    descending_order(single_string)
    print("============= END ===============")
    return
