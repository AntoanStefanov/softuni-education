from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        food = None
        if food_type == 'Bread':
            food = Bread(name, price)
        elif food_type == 'Cake':
            food = Cake(name, price)

        if food:
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = None
        if drink_type == 'Tea':
            drink = Tea(name, portion, brand)
        elif drink_type == 'Water':
            drink = Water(name, portion, brand)
        if drink:
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        table = None
        if table_type == 'InsideTable':
            table = InsideTable(table_number, capacity)
        elif table_type == 'OutsideTable':
            table = OutsideTable(table_number, capacity)

        if table:
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        for table in self.tables_repository:
            if table.table_number == table_number:
                in_menu = []
                not_in_menu = []
                for food in food_names:
                    for food_in_menu in self.food_menu:
                        if food == food_in_menu.name:
                            in_menu.append(food_in_menu)
                            table.food_orders.append(food_in_menu)
                            break
                    else:
                        not_in_menu.append(food)
                if in_menu or not_in_menu:
                    info = ''
                    if in_menu:
                        info += f'Table {table_number} ordered:\n'
                        for food in in_menu:
                            info += f'{repr(food)}\n'
                    if not_in_menu:
                        info += f'{self.name} does not have in the menu:\n'
                        for food in not_in_menu:
                            info += f'{food}\n'
                    return info[:-1]
        return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *drink_names):
        for table in self.tables_repository:
            if table.table_number == table_number:
                in_menu = []
                not_in_menu = []
                for drink in drink_names:
                    for drink_in_menu in self.drinks_menu:
                        if drink == drink_in_menu.name:
                            in_menu.append(drink_in_menu)
                            table.drink_orders.append(drink_in_menu)
                            break
                    else:
                        not_in_menu.append(drink)
                if in_menu or not_in_menu:
                    info = ''
                    if in_menu:
                        info += f'Table {table_number} ordered:\n'
                        for drink in in_menu:
                            info += f'{repr(drink)}\n'
                    if not_in_menu:
                        info += f'{self.name} does not have in the menu:\n'
                        for drink in not_in_menu:
                            info += f'{drink}\n'
                    return info
        return f"Could not find table {table_number}"

    def leave_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                bill = table.get_bill()
                self.total_income += bill
                table.clear()

                info = f'Table: {table_number}\n'
                info += f'Bill: {bill + 0.01:.2f}'
                return info

    def get_free_tables_info(self):
        info = ''
        for table in self.tables_repository:
            res = table.free_table_info()
            if res:
                info += f'{res}\n'  # 42 test
        return info[:-1]

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
