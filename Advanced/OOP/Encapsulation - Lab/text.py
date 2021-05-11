class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        print('hi')
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.fullname = name


emp_1 = Employee('Tony', 'Morrata')

emp_1.fullname = 'Akzaran Toshev'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
