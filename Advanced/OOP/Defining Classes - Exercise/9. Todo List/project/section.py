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
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        index = 0
        removed_tasks = 0
        while index < len(self.tasks):
            current_task = self.tasks[index]
            if current_task.completed:
                self.tasks.remove(current_task)
                removed_tasks += 1
                continue
            index += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        view = f'Section {self.name}:\n'
        for task in self.tasks:
            view += f'{task.details()}\n'
        return view
