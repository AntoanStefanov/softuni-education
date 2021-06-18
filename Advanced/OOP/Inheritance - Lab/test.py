class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.age = age

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, age, pay, programing_language):
        super().__init__(first, last, age, pay)
        self.programing_language = programing_language

    def __repr__(self):
        return ' : '.join(f'{key} - {value}' for key, value in self.__dict__.items())


class Manager(Employee):

    # None,  bcs you never wanna pass mutable data type like list as default arg
    def __init__(self, first, last, age, pay, supervising_team=None):
        super().__init__(first, last, age, pay)
        if supervising_team is None:
            self.supervising_team = []
        else:
            self.supervising_team = supervising_team

    def add_employee(self, employee):
        if employee not in self.supervising_team:
            self.supervising_team.append(employee)
            return 'Added to the team'
        return 'Already in that team'

    def remove_employee(self, employee):
        if employee in self.supervising_team:
            self.supervising_team.remove(employee)
            return 'Removed from the team'
        return 'Not found in that team'

    def print_team(self):
        for emp in self.supervising_team:
            print(f'--->{emp.full_name()}')


dev_1 = Developer('Tony', 'Stefanov', 20, 100000, 'C')
dev_2 = Developer('Roy', 'Stoy', 20,  1000, 'Python')

dev_1.age = 30
print(dev_1.age)
print(dev_1)

man_1 = Manager('Tony', 'Zozo', 21, 100000)

print(man_1.age)
# isinstance # if an object is an instance of a class
print(isinstance(man_1, Developer))

print(issubclass(Developer, Employee))
