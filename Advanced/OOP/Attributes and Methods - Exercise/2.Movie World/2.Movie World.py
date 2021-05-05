class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        dvd_names = []
        for rented_dvd in self.rented_dvds:
            dvd_names.append(rented_dvd.name)
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(dvd_names)})"


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def get_month(month):
        months = {'1': 'January', '2': 'February', '3': 'March', '4': 'April',
                  '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September',
                  '10': 'October', '11': 'November', '12': 'December'}
        return months[month]

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        month, year = date.split('.')[1:]
        year = int(year)
        month = cls.get_month(month)
        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = 'rented'
        else:
            status = 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd.is_rented:
                            return f"{customer.name} has already rented {dvd.name}"
                        if customer.age < dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                        customer.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f"{customer.name} has successfully rented {dvd.name}"

            else:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd.is_rented:
                            return "DVD is already rented"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f"{customer.name} has successfully returned {dvd.name}"
                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        representation = ''
        for c in self.customers:
            representation += f'{c}\n'
        for d in self.dvds:
            representation += f'{d}\n'
        return representation


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))


print(movie_world)
