from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        # int both consumptions ? bcs it returns floats
        super().__init__(name, 'Light', capacity_consumption * 1.5, memory_consumption * 0.5)
