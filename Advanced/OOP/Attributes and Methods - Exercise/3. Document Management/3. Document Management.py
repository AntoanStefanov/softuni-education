class Topic:
    def __init__(self, id, topic, storage_folder):
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic, new_storage_folder):
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"


class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def edit(self, new_name):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"