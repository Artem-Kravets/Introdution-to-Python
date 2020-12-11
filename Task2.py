my_string = input()


def replace_every_duplicate_of_first_letter(a):
    first_letter = a[0]
    return first_letter + a[1:].replace(first_letter, "_")


print(replace_every_duplicate_of_first_letter(my_string))

