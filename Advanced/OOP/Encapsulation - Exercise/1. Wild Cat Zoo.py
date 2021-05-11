class Lion:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def get_needs(): return 50

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Tiger:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def get_needs(): return 45

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Cheetah:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def get_needs(): return 60

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Keeper:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Caretaker:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Vet:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    def total_salary_cost(self):
        total_cost = 0
        for worker in self.workers:
            total_cost += worker.salary
        return total_cost

    def get_all_animals_needs(self):
        all_animals_needs = 0
        for animal in self.animals:
            all_animals_needs += animal.get_needs()
        return all_animals_needs

    def add_animal(self, animal, price):
        if self.__budget - price < 0:
            return "Not enough budget"
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary_cost = self.total_salary_cost()
        if self.__budget >= total_salary_cost:
            self.__budget -= total_salary_cost
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        all_animals_needs = self.get_all_animals_needs()
        if self.__budget >= all_animals_needs:
            self.__budget -= all_animals_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

# -	Returns the following string:
# You have {total_animals_count} animals
# ----- {amount_of_lions} Lions:
# {lion1}
# …
# ----- {amount_of_tigers} Tigers:
# {tiger1}
# …
# ----- {amount_of_cheetahs} Cheetahs:
# {cheetah1}
# …

    def animals_status(self):
        status = ''
        lions = [animal for animal in self.animals if type(
            animal).__name__ == 'Lion']
        tigers = [animal for animal in self.animals if type(
            animal).__name__ == 'Tiger']
        cheetahs = [animal for animal in self.animals if type(
            animal).__name__ == 'Cheetah']

        status += f'You have {len(self.animals)} animals\n'
        status += f'----- {len(lions)} Lions:\n'
        for lion in lions:
            status += f'{lion}\n'
        status += f'----- {len(tigers)} Tigers:\n'
        for tiger in tigers:
            status += f'{tiger}\n'
        status += f'----- {len(cheetahs)} Cheetahs:\n'
        for ch in cheetahs:
            status += f'{ch}\n'
        return status

    def workers_status(self):
        pass


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion(
    "Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker(
    "Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
# print(zoo.workers_status())
