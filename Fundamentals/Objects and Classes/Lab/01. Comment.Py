class Party:
    def __init__(self):
        self.people = []

    def going_person(self, name):
        self.people.append(name)

    def party_started(self):
        print("Going: " + ", ".join(self.people))
        print(f"Total: {len(self.people)}")


party1 = Party()


while True:
    name = input()
    if name == "End":
        break
    party1.going_person(name)


party1.party_started()
