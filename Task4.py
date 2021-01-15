def my_generator(input_string, max_times, step=1):
    words = input_string.split(" ")
    index = 0
    inner_index = 0
    while inner_index < max_times:
        yield words[index]
        index = (index + 1) % len(words)
        inner_index += step


my_gen = my_generator("Winter Spring Summer Autumn", 9)

for i in my_gen:
    print(i)
