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
    def __init__(self, date, customer_id, trainer_id, exercise_id):
        pass
