import math

class TimeMachineAI:
    def __init__(self):
        self.time_machine_components = []

    def add_component(self, component):
        self.time_machine_components.append(component)

    def remove_component(self, component):
        self.time_machine_components.remove(component)

    def get_time_machine_schematics(self):
        schematics = ""
        for component in self.time_machine_components:
            schematics += component.to_schematic() + "\n"
        return schematics

class TimeMachineComponent:
    def __init__(self, name, material, dimensions):
        self.name = name
        self.material = material
        self.dimensions = dimensions

    def to_schematic(self):
        schematic = f"Component: {self.name}\n"
        schematic += f"Material: {self.material}\n"
        schematic += f"Dimensions: {','.join(map(str, self.dimensions))}\n"
        return schematic

class TimeMachineFormula:
    def __init__(self, formula):
        self.formula = formula

    def calculate(self, variables):
        return eval(self.formula, variables)

class TimeMachineUtils:
    @staticmethod
    def calculate_distance(time_travel_speed, time_elapsed):
        return time_travel_speed * time_elapsed

    @staticmethod
    def calculate_time_elapsed(distance, time_travel_speed):
        return distance / time_travel_speed

    @staticmethod
    def calculate_space_distance(space_travel_speed, space_elapsed):
        return space_travel_speed * space_elapsed

    @staticmethod
    def calculate_space_elapsed(space_distance, space_travel_speed):
        return space_distance / space_travel_speed

    @staticmethod
    def calculate_time_dilation(time_elapsed, velocity):
        return math.sqrt(1 - (velocity ** 2)) * time_elapsed

    @staticmethod
    def calculate_velocity(time_dilation, time_elapsed):
        return math.sqrt(1 - ((time_dilation / time_elapsed) ** 2))

def main():
    # Create a TimeMachineAI object
    time_machine_ai = TimeMachineAI()

    # Create TimeMachineComponent objects and add them to TimeMachineAI
    component1 = TimeMachineComponent("Time Engine", "Platinum", (10, 20, 30))
    component2 = TimeMachineComponent("Space Field Generator", "Titanium", (15, 25, 35))
    time_machine_ai.add_component(component1)
    time_machine_ai.add_component(component2)

    # Retrieve the time machine schematics
    schematics = time_machine_ai.get_time_machine_schematics()
    print(schematics)

    # Define the custom functions to be used in the formula calculation
    variables = {
        "calculate_distance": TimeMachineUtils.calculate_distance,
        "calculate_velocity": TimeMachineUtils.calculate_velocity,
    }

    # Create a TimeMachineFormula object and calculate distance traveled
    formula = "calculate_distance(100, 5)"
    tm_formula = TimeMachineFormula(formula)
    distance = tm_formula.calculate(variables)
    print(f"Distance traveled: {distance}")

    # Calculate velocity using time dilation and time_elapsed
    velocity_formula = "calculate_velocity(2, 10)"
    velocity_formula_obj = TimeMachineFormula(velocity_formula)
    velocity = velocity_formula_obj.calculate(variables)
    print(f"Velocity: {velocity}")

if __name__ == "__main__":
    main()