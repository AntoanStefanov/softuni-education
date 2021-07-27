from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]  # Ako nqma hardware IndexError
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return 'Hardware does not exist'
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]  # Ako nqma hardware IndexError
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return 'Hardware does not exist'
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)  # Тук махаве софтуера от системата с всички софтуери
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        analyze = 'System Analysis\n'
        analyze += f'Hardware Components: {len(System._hardware)}\n'
        analyze += f'Software Components: {len(System._software)}\n'
        analyze += f'Total Operational Memory: {sum([hardware.used_memory for hardware in System._hardware])} / {sum([h.memory for h in System._hardware])}\n'
        analyze += f'Total Capacity Taken: {sum([hardware.used_capacity for hardware in System._hardware])} / {sum([h.capacity for h in System._hardware])}'
        return analyze

    @staticmethod
    def system_split():
        system = ''
        for hardware in System._hardware:
            system += f'Hardware Component - {hardware.name}\n'
            express_software_components = [software for software in hardware.software_components if
                                           type(software).__name__ == "ExpressSoftware"]
            system += f'Express Software Components: {len(express_software_components)}\n'
            light_software_components = [software for software in hardware.software_components if
                                         type(software).__name__ == "LightSoftware"]
            system += f'Light Software Components: {len(light_software_components)}\n'
            system += f'Memory Usage: {hardware.used_memory} / {hardware.memory}\n'
            system += f"Capacity Usage: {hardware.used_capacity} / {hardware.capacity}\n"
            system += f'Type: {hardware.type}\n'
            software_components_names = ', '.join([software.name for software in hardware.software_components])
            # Е ТУК , С 66 ред са залепени иначе не минава, грешка в задачата. Ппц е нужено \n ,но не минава така
            system += f'Software Components: {software_components_names if software_components_names else None}'

        return system
