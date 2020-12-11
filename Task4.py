print("Task №4:")
words = ["radar", "device", "level", "program", "kayak", "river", "racecar"]
my_list = []


def get_polynomials_from_list(a):
    for elements in a:
        if elements == elements[::-1]:
            my_list.append(elements)
    return print(my_list)


get_polynomials_from_list(words)
