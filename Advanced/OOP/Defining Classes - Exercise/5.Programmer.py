class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        return f'{self.name} does not know {language}'

    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed and new_language != self.language:
            res = f'{self.name} switched from {self.language} to {new_language}'
            self.language = new_language
            return res
        if self.skills >= skills_needed and new_language == self.language:
            return f'{self.name} already knows {self.language}'
        if self.skills < skills_needed:
            return f'{self.name} needs {skills_needed - self.skills} more skills'


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
