# Tuk moje auto incrementing posotion of the person vmesto da si igraq sus samite indexi
# Kato stignesh go naprai, ok ?
# Class attribute number of person i v inita kato se syzdade nov += 1


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f'{self.name} {self.surname}'


class Group:
    def __init__(self, name, people: list):
        self.name = name
        self.people = people

    def __getitem__(self, index):
        return f'Person {index}: {self.people[index]}'

    def __add__(self, other):
        all_people = self.people + other.people
        return Group(self.name, all_people)

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        members = [f'{person.name} {person.surname}' for person in self.people]
        return f'Group {self.name} with members {", ".join(members)}'

    def __iter__(self):
        return iter(self.people)


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])

third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for index, person in enumerate(third_group): # Procheti gore kvo pishe
    print(f'Person {index}: {person}')
