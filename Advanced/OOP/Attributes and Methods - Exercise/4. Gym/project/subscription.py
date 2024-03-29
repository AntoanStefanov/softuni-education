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
