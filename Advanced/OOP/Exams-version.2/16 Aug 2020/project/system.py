from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        if power_hardware not in System._hardware:
            System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        if heavy_hardware not in System._hardware:  # unnecessary if maybe ?
            System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                try:
                    hardware.install(express_software)
                    System._software.append(express_software)
                except Exception as ex:
                    return str(ex)
        return 'Hardware does not exist'

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                light_software = LightSoftware(name, capacity_consumption, memory_consumption)
                try:
                    hardware.install(light_software)
                    System._software.append(light_software)
                except Exception as ex:
                    return str(ex)
                return
        return 'Hardware does not exist'

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                for software in System._software:
                    if software.name == software_name:
                        if software in hardware.software_components:
                            hardware.uninstall(software)
                            System._software.remove(software)
                            return
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        analyze = 'System Analysis\n'
        analyze += f'Hardware Components: {len(System._hardware)}\n'
        analyze += f'Software Components: {len(System._software)}\n'
        total_memory = sum([hardware.memory for hardware in System._hardware])
        total_used_memory = sum([hardware.used_memory for hardware in System._hardware])
        analyze += f'Total Operational Memory: {total_used_memory} / {total_memory}\n'
        total_capacity = sum([hardware.capacity for hardware in System._hardware])
        total_used_capacity = sum([hardware.used_capacity for hardware in System._hardware])
        analyze += f'Total Capacity Taken: {total_used_capacity} / {total_capacity}'

        return analyze

    @staticmethod
    def system_split():
        system = ''
        for hardware in System._hardware:
            system += f'Hardware Component - {hardware.name}\n'
            express = 0
            light = 0
            for software in hardware.software_components:
                if software.type == 'Express':
                    express += 1
                elif software.type == 'Light':
                    light += 1
            system += f'Express Software Components: {express}\n'
            system += f'Light Software Components: {light}\n'
            system += f'Memory Usage: {int(hardware.used_memory)} / {int(hardware.memory)}\n'
            system += f'Capacity Usage: {int(hardware.used_capacity)} / {int(hardware.capacity)}\n'
            system += f'Type: {hardware.type}\n'
            if hardware.software_components:
                softwares = []
                for software in hardware.software_components:
                    softwares.append(software.name)
                softwares = ', '.join(softwares)
                system += f"Software Components: {softwares}"
            else:
                system += 'Software Components: None'
        return system
