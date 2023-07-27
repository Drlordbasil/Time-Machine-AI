import random

class TimeMachine:
    def __init__(self, name):
        self.name = name
        self.schematics = {}

    def add_component(self, component):
        if component.category in self.schematics:
            self.schematics[component.category].append(component.name)
        else:
            self.schematics[component.category] = [component.name]

    def generate_schematics(self):
        print(f"Schematics for {self.name}:")
        for category, components in self.schematics.items():
            print(f"{category}:")
            for component in components:
                print(f"- {component}")
        print("Schematics generated successfully!")

class Component:
    def __init__(self, name, category):
        self.name = name
        self.category = category

def generate_random_component():
    categories = ["Power", "Control", "Navigation", "Time Manipulation"]
    names = ["Flux Capacitor", "Temporal Displacement Device", "Quantum Processor", "Wormhole Generator",
             "Time Coils", "Chrono Circuit", "Temporal Flux Absorber", "Dimensional Stabilizer"]
    category = random.choice(categories)
    name = random.choice(names)
    return Component(name, category)

def main():
    time_machine = TimeMachine("Time-Machine-AI")

    for _ in range(10):
        component = generate_random_component()
        time_machine.add_component(component)

    time_machine.generate_schematics()

if __name__ == "__main__":
    main()