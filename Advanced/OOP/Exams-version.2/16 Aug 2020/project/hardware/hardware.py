from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def used_memory(self):
        return sum([software.memory_consumption for software in self.software_components])

    @property
    def used_capacity(self):
        return sum([software.capacity_consumption for software in self.software_components])

    def install(self, software: Software):
        if self.capacity - self.used_capacity >= software.capacity_consumption and \
                self.capacity - self.used_memory >= software.memory_consumption:
            self.software_components.append(software)
        else:
            raise Exception('Software cannot be installed')

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
