my_string = input()


def cut_the_string(a):
    if len(a) < 2:
        return "''"
    else:
        return a[:2] + a[-2:]


print(cut_the_string(my_string))
