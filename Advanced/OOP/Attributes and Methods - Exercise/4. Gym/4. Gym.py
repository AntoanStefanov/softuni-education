class Customer:
    customer_id = 0

    def __init__(self, name, address, email):
        Customer.customer_id += 1
        self.name = name
        self.address = address
        self.email = email
        self.customer_id = Customer.customer_id

    def __repr__(self):
        return f"Customer <{self.customer_id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.customer_id + 1


class Equipment:
    equipment_id = 0

    def __init__(self, name):
        Equipment.equipment_id += 1
        self.name = name
        self.equipment_id = Equipment.equipment_id

    def __repr__(self):
        return f"Equipment <{self.equipment_id}> {self.name}"


class ExercisePlan:
    exercise_plan_id = 0

    def __init__(self, trainer_id, equipment_id, duration):
        ExercisePlan.exercise_plan_id += 1
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration  # in minutes
        self.exercise_plan_id = ExercisePlan.exercise_plan_id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        cls(trainer_id, equipment_id, hours * 60)

    @staticmethod
    def get_next_id():
        return ExercisePlan.exercise_plan_id + 1

    def __repr__(self):
        return f"Plan <{self.exercise_plan_id}> with duration {self.duration} minutes"


class Subscription:
    subscription_id = 0

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        Subscription.subscription_id += 1
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.subscription_id = Subscription.subscription_id

    @staticmethod
    def get_next_id():
        return Subscription.subscription_id + 1

    def __repr__(self):
        return f"Subscription <{self.exercise_id}> on {self.date}"

class Trainer:
    trainer_id = 0

    def __init__(self, name):
        Trainer.trainer_id += 1
        self.name = name
        self.trainer_id = Trainer.trainer_id
    
    def __repr__(self):
        return f"Trainer <{self.trainer_id}> {self.name}"

    def get_next_id(self):
        return Trainer.trainer_id


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer): 
        if customer not in self.customers:
            self.customers.append(customer)
    
    def add_trainer(self, trainer: Trainer): 
        if trainer not in self.trainers:
            self.trainers.append(trainer)




customer = Customer("John", "Maple Street", "john.smith@gmail.com")
print(customer)
print(customer.get_next_id())
