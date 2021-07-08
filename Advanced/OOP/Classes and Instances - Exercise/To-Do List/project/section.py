class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        tasks_to_remove = []
        for task in self.tasks:
            if task.completed:
                tasks_to_remove.append(task)
        amount = len(tasks_to_remove)
        while tasks_to_remove:
            task_to_remove = tasks_to_remove.pop(0)
            self.tasks.remove(task_to_remove)
        return f"Cleared {amount} tasks."

    def view_section(self):
        view = f"Section {self.name}:"
        for task in self.tasks:
            view += f'\n{task.details()}'  
        return view