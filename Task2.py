print("Task №2:")
my_list = ["111111", "123456", "Olga", "Anastasia", "Vladimir", "Natalya", "Andrew"]

search = lambda my_list: [word for word in my_list if len(word) == 6]

print(search(my_list))
