class Sentence:

    def __init__(self, input_string, step=1):
        self.words = input_string.split(" ")
        self.value = 0
        self.end = len(self.words)
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        output = self.words[self.value]
        self.value += self.step
        return output


my_iter = Sentence("Hello this beautiful world")

for i in my_iter:
    print(i)
