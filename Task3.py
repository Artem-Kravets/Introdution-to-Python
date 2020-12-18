class Human:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Employee(Human):

    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name, salary)

    @staticmethod
    def from_string(my_string):
        if type(my_string) is str:
            my_list = my_string.split("-")
            if len(my_list) != 3:
                raise Exception("Error! \n Enter employee in format: 'Name'-'Surname'-'Salary'")
            else:
                my_employee = Employee(my_list[0], my_list[1], my_list[2])
                return my_employee
        else:
            raise Exception("Error! \n Not str type")


emp1 = Employee('JOAN', 'Smith', 85000)
emp2 = Employee.from_string('John-doe-73000')
print(emp1.first_name)
print(emp1.full_name())
print(emp1.salary)
print(emp2.first_name)
print(emp2.full_name())
print(emp2.salary)



