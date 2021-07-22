class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def left_capacity(self):
        return self.capacity - self.used_capacity

    @property
    def left_memory(self):
        return self.memory - self.used_memory

    @property
    def used_capacity(self):
        taken_capacity = 0
        for software_component in self.software_components:
            taken_capacity += software_component.capacity_consumption
        return taken_capacity

    @property
    def used_memory(self):
        taken_memory = 0
        for software_component in self.software_components:
            taken_memory += software_component.memory_consumption
        return taken_memory

    def install(self, software):

        if self.left_capacity >= software.capacity_consumption and self.left_memory >= software.memory_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)
