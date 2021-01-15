class Circle:

    def __init__(self, seasons, max_range):
        self.seasons = seasons.split(" ")
        self.max_range = max_range

    def __iter__(self):
        return CircleIterator(self)


class CircleIterator:

    def __init__(self, circle):
        self.my_circle = circle
        self.inner_index = 0
        self.index = 0

    def __next__(self):
        if self.inner_index >= self.my_circle.max_range:
            raise StopIteration
        output = self.my_circle.seasons[self.index]
        self.index = (self.index + 1) % len(self.my_circle.seasons)
        self.inner_index += 1
        return output


my_circle = Circle("Winter Spring Summer Autumn", 7)


for i in my_circle:
    print(i)

    
