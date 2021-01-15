def my_generator(input_string, step=1):
    words = input_string.split(" ")
    index = 0
    while index < len(words):
        yield words[index]
        index += step


my_gen = my_generator("Hello this beautiful world")

for i in my_gen:
    print(i)
