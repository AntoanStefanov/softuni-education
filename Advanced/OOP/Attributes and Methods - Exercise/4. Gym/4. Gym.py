class Customer:
    customer_id = 0

    def __init__(self, name, address, email):
        Customer.customer_id += 1
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.customer_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.customer_id + 1


class Equipment:
    equipment_id = 0

    def __init__(self, name):
        Equipment.equipment_id += 1
        self.name = name
        self.id = Equipment.equipment_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.equipment_id + 1


class ExercisePlan:
    exercise_plan_id = 0

    def __init__(self, trainer_id, equipment_id, duration):
        ExercisePlan.exercise_plan_id += 1
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.exercise_plan_id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)

    @staticmethod
    def get_next_id():
        return ExercisePlan.exercise_plan_id + 1

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"


class Subscription:
    subscription_id = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        Subscription.subscription_id += 1
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.subscription_id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @staticmethod
    def get_next_id():
        return Subscription.subscription_id + 1


class Trainer:
    trainer_id = 0

    def __init__(self, name):
        Trainer.trainer_id += 1
        self.name = name
        self.id = Trainer.trainer_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.trainer_id + 1


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [
            subscription
            for subscription in self.subscriptions
            if subscription.id == subscription_id
        ][0]

        customer = [
            customer
            for customer in self.customers
            if customer.id == subscription.customer_id
        ][0]

        trainer = [
            trainer
            for trainer in self.trainers
            if trainer.id == subscription.trainer_id
        ][0]

        plan = [
            plan
            for plan in self.plans
            if plan.trainer_id == trainer.id
        ][0]

        equipment = [
            equipment
            for equipment in self.equipment
            if equipment.id == plan.equipment_id
        ][0]

        return f'{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}'


customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
