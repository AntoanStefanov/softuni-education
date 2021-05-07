class Customer:
    customer_id = 0

    def __init__(self, name, address, email):
        Customer.customer_id += 1
        self.name = name
        self.address = address
        self.email = email
        self.customer_id = Customer.customer_id

    def __repr__(self):
        return f"Customer <{self.customer_id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.customer_id + 1


class Equipment:
    equipment_id = 0

    def __init__(self, name):
        Equipment.equipment_id += 1
        self.name = name
        self.equipment_id = Equipment.equipment_id


customer = Customer("John", "Maple Street", "john.smith@gmail.com")
print(customer)
print(customer.get_next_id())
