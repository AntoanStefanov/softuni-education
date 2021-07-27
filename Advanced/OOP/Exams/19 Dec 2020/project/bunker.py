from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        f = [supply for supply in self.supplies if type(supply).__name__ == 'FoodSupply']
        if f:
            return f
        raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        w = [supply for supply in self.supplies if type(supply).__name__ == 'WaterSupply']
        if w:
            return w
        raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        pk = [med for med in self.medicine if type(med).__name__ == 'Painkiller']
        if pk:
            return pk
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        s = [med for med in self.medicine if type(med).__name__ == 'Salve']
        if s:
            return s
        raise IndexError("There are no salves left!")

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, med):
        self.medicine.append(med)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            medicine = None
            if medicine_type == 'Painkiller':
                medicine = self.painkillers.pop(-1)
            elif medicine_type == 'Salve':
                medicine = self.salves.pop(-1)
            self.medicine.remove(medicine)
            medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            s = None
            if sustenance_type == 'FoodSupply':
                s = self.food.pop(-1)
            elif sustenance_type == 'WaterSupply':
                s = self.water.pop(-1)
            self.supplies.remove(s)
            s.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
            self.sustain(s, 'WaterSupply')
            self.sustain(s, 'FoodSupply')


# bunker = Bunker()
#
# pk = Painkiller()
# pk1 = Painkiller()
# pk2 = Painkiller()
# sal = Salve()
# sal1 = Salve()
# sal2 = Salve()
#
#
# bunker.add_medicine(pk)
# bunker.add_medicine(sal)
# bunker.add_medicine(pk1)
# bunker.add_medicine(sal1)
# bunker.add_medicine(pk2)
#
# sur = Survivor('Tony', 20)
# sur.health = 50
#
# print(bunker.medicine)
# print(bunker.painkillers)
# bunker.heal(sur, 'Painkiller')