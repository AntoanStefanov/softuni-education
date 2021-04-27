class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if new_name == self.name:
            return "Name cannot be the same."
        self.name = new_name
        return new_name

    def change_due_date(self, new_due: str):
        if new_due == self.due_date:
            return 'Date cannot be the same.'
        self.due_date = new_due
        return new_due

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if 0 <= comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        return "Cannot find comment."

    def details(self):
        return f'Name: {self.name} - Due Date: {self.due_date}'


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
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


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
