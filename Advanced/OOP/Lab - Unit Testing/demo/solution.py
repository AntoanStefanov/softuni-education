class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.second_name}"

    def get_info(self):
        return f"{self.first_name} {self.second_name} is {self.age}"
