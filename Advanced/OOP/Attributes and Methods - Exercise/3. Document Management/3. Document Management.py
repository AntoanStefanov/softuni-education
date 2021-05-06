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


class Document:
    def __init__(self, id, category_id, topic_id, file_name):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str):
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content):
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content):
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, new_file_name):
        self.file_name = new_file_name

    def __repr__(self):
        return f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {', '.join(self.tags)}"

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    
    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)    
        

    def edit_category(self, category_id: int, new_name:str):
        for category in self.categories:
            if category.id == category_id:
                category.edit(new_name)
                return 
    
    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.edit(new_topic, new_storage_folder)
                return 
    
    def edit_document(self, document_id: int, new_file_name: str):
        for document in self.documents:
            if document.id == document_id:
                document.edit(new_file_name)
                break