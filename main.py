import random


class TimeMachineAI:
    """
    A class representing a Time Machine AI.
    """

    def __init__(self):
        """
        Initialize a TimeMachineAI object.
        """
        self.dimensions = ["Length", "Width", "Height"]
        self.materials = ["Steel", "Aluminum", "Titanium"]
        self.power_sources = [
            "Nuclear Fusion Reactor",
            "Antimatter Annihilation Chamber",
            "Zero-Point Energy Extractor"
        ]
        self.components = [
            "Temporal Displacement Coil",
            "Chrono-Vector Stabilizer",
            "Quantum Flux Compensator"
        ]

    def generate_schematic(self):
        """
        Generate a schematic for the Time Machine.
        Returns:
            A string representing the Time Machine schematic.
        """
        dimensions_values = {dimension: random.randint(10, 100) for dimension in self.dimensions}
        materials_sample = random.sample(self.materials, 3)
        power_source = random.choice(self.power_sources)

        schematic = "Time Machine Schematic:\n"
        schematic += "-----------------------\n\n"
        schematic += "Dimensions:\n"
        schematic += "\n".join([f"{dimension}: {value} meters" for dimension, value in dimensions_values.items()])
        schematic += "\n\nMaterials:\n"
        schematic += "\n".join(materials_sample) + "\n\n"
        schematic += "Power Source:\n"
        schematic += power_source + "\n\n"
        schematic += "Components:\n"
        schematic += "\n".join(self.components) + "\n\n"

        return schematic


def main():
    """
    The main function.
    """
    tm_ai = TimeMachineAI()
    schematic = tm_ai.generate_schematic()
    print(schematic)


if __name__ == "__main__":
    main()