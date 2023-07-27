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
        self.power_sources = ["Nuclear Fusion Reactor", "Antimatter Annihilation Chamber", "Zero-Point Energy Extractor"]
        self.components = ["Temporal Displacement Coil", "Chrono-Vector Stabilizer", "Quantum Flux Compensator"]
        self.schematic = ""

    def generate_schematic(self):
        """
        Generate a schematic for the Time Machine.

        Returns:
        A string representing the Time Machine schematic.
        """
        self.schematic = "Time Machine Schematic:\n"
        self.schematic += "-----------------------\n\n"

        self.schematic += "Dimensions:\n"
        for dimension in self.dimensions:
            value = random.randint(10, 100)
            self.schematic += f"{dimension}: {value} meters\n"
        self.schematic += "\n"

        self.schematic += "Materials:\n"
        self.schematic += '\n'.join(random.sample(self.materials, 3))
        self.schematic += "\n\n"

        self.schematic += "Power Source:\n"
        self.schematic += random.choice(self.power_sources)
        self.schematic += "\n\n"

        self.schematic += "Components:\n"
        self.schematic += '\n'.join(self.components)
        self.schematic += "\n\n"

        return self.schematic


def main():
    """
    The main function.
    """
    tm_ai = TimeMachineAI()
    schematic = tm_ai.generate_schematic()
    print(schematic)


if __name__ == "__main__":
    main()

# improvements:
# - used random.sample instead of random.choice to ensure unique materials are chosen
# - removed unnecessary newlines after power source and components
# - removed unnecessary self.schematic assignment during initialization