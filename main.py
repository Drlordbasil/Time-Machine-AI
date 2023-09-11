import math

class TimeMachineAI:
    def __init__(self):
        self.schematics = {}
        self.formulas = {}
    
    def add_schematic(self, name, schematic):
        self.schematics[name] = schematic
    
    def remove_schematic(self, name):
        del self.schematics[name]
    
    def get_schematic(self, name):
        return self.schematics.get(name, None)
    
    def add_formula(self, name, formula):
        self.formulas[name] = formula
    
    def remove_formula(self, name):
        del self.formulas[name]
    
    def get_formula(self, name):
        return self.formulas.get(name, None)
    
    def calculate_time_travel(self, formula_name, values):
        formula = self.get_formula(formula_name)
        if formula is not None:
            try:
                x = eval(formula, {}, values)
                return round(x, 2)
            except:
                return None
        else:
            return None
    

# Example usage

# Create an instance of the TimeMachineAI
time_machine_ai = TimeMachineAI()

# Add schematics for different time machine models
time_machine_ai.add_schematic("Model 1", "Schematic 1")
time_machine_ai.add_schematic("Model 2", "Schematic 2")

# Get schematic for a time machine model
schematic = time_machine_ai.get_schematic("Model 1")
print("Schematic for Model 1:", schematic)

# Remove a schematic
time_machine_ai.remove_schematic("Model 2")

# Add formulas for time travel calculations
time_machine_ai.add_formula("Formula 1", "x**2 + y")
time_machine_ai.add_formula("Formula 2", "math.sin(x) + math.cos(y)")

# Get formula for time travel calculation
formula = time_machine_ai.get_formula("Formula 1")
print("Formula 1:", formula)

# Calculate time travel using a formula
values = {'x': 5, 'y': 3}
result = time_machine_ai.calculate_time_travel("Formula 1", values)
print("Time travel result:", result)