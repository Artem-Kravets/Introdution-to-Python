print("Task №3:")
weekdays = ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
days = [7, 6, 5, 4, 3, 2, 1]


def get_date(a, b):
    return sorted(list(zip(a, b)), key=lambda sort_by_second_element: sort_by_second_element[1])


print(get_date(weekdays, days))


# def get_date(a, b):
#     return list(reversed(list(zip(a, b))))
#
#
# print(get_date(weekdays, days))


# def get_date(a, b):
#     a.reverse()
#     b.reverse()
#     return list(zip(a, b))
#
#
# print(get_date(weekdays, days))
