from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        # int both consumptions ? bcs it returns floats
        super().__init__(name, 'Express', capacity_consumption, memory_consumption * 2)

