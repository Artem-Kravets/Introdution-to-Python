print("Task №5:")
my_list = [1, 2, [3, 4], [5, 6, [7, 8, 9, 10]]]


def sum_elements_of_list(a):
    return a if type(a) is int else sum([sum_elements_of_list(b) for b in a])


print(sum_elements_of_list(my_list))
