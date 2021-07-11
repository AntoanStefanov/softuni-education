class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    # change logic.
    def add_animal(self, animal, price):
        if self.__budget - price >= 0 and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        if len(self.animals) < self.__animal_capacity and self.__budget - price < 0:
            return "Not enough budget"
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def sum_total_salaries(self):
        sum_ = 0
        for worker in self.workers:
            sum_ += worker.salary
        return sum_

    def pay_workers(self):
        total_salaries = self.sum_total_salaries()
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def sum_animal_cost(self):
        cost = 0
        for animal in self.animals:
            cost += animal.money_for_care
        return cost

    def tend_animals(self):
        animals_cost = self.sum_animal_cost()
        if self.__budget >= animals_cost:
            self.__budget -= animals_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if type(
            animal).__name__ == 'Lion']
        tigers = [animal for animal in self.animals if type(
            animal).__name__ == 'Tiger']
        cheetahs = [animal for animal in self.animals if type(
            animal).__name__ == 'Cheetah']

        res = f'You have {len(self.animals)} animals'
        res += f'\n----- {len(lions)} Lions:'
        for lion in lions:
            res += f'\n{lion}'
        res += f'\n----- {len(tigers)} Tigers:'
        for tiger in tigers:
            res += f'\n{tiger}'
        res += f'\n----- {len(cheetahs)} Cheetahs:'
        for cheetah in cheetahs:
            res += f'\n{cheetah}'
        return res

    def workers_status(self):
        keepers = [worker for worker in self.workers if type(
            worker).__name__ == 'Keeper']
        caretakers = [worker for worker in self.workers if type(
            worker).__name__ == 'Caretaker']
        vets = [worker for worker in self.workers if type(
            worker).__name__ == 'Vet']

        res = f'You have {len(self.workers)} workers'
        res += f'\n----- {len(keepers)} Keepers:'
        for keeper in keepers:
            res += f'\n{keeper}'
        res += f'\n----- {len(caretakers)} Caretakers:'
        for caretaker in caretakers:
            res += f'\n{caretaker}'
        res += f'\n----- {len(vets)} Vets:'
        for vet in vets:
            res += f'\n{vet}'
        return res
