my_string = input()


def find_words_with_letters_and_numbers(a):
    final_list = []
    new_list = a.split()
    for i in new_list:
        if i.isalnum() and not i.isalpha() and not i.isdigit():
            final_list.append(i)
    return final_list


print(find_words_with_letters_and_numbers(my_string))
