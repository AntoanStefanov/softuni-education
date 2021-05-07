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

    def edit_category(self, category_id: int, new_name: str):
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

    def delete_category(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove(category)
                return

    def delete_topic(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                self.topics.remove(topic)
                return

    def delete_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                self.documents.remove(document)
                return

    def get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        representation = ''
        for document in self.documents:
            representation += f'{document}\n'
        return representation
