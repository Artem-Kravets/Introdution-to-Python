class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order_number += 1
        self.order_number = Pizza.order_number

    @staticmethod
    def pepperoni():
        return Pizza(['bacon', 'mozzarella', 'oregano'])

    @staticmethod
    def hawaiian():
        return Pizza(['ham', 'pineapple'])

    @staticmethod
    def margherita():
        return Pizza(['mozzarella', 'olives', 'tomatoes'])


p1 = Pizza(['bacon', 'parmesan', 'ham'])  # order1
p2 = Pizza.pepperoni()  # order2

print(p1.ingredients)
print(p2.ingredients)

print(p1.order_number)
print(p2.order_number)
