import random
from datetime import datetime

class TimeMachineAI:
    
    def __init__(self, name):
        self.name = name
        self.colors = ["red", "blue", "green", "yellow", "orange"]
    
    def create_schematics(self):
        schematic = ""
        
        schematic += self.generate_header()
        schematic += self.generate_power_supply()
        schematic += self.generate_time_circuits()
        schematic += self.generate_flux_capacitor()
        schematic += self.generate_dimensional_field_generator()
        schematic += self.generate_housing()
        schematic += self.generate_controls()
        schematic += self.generate_ancillary_systems()
        schematic += self.generate_fuel_system()
        schematic += self.generate_navigation_system()
        schematic += self.generate_protective_systems()
        schematic += self.generate_finish()
        
        return schematic
    
    def generate_header(self):
        header = "Time Machine Schematics\n\n"
        header += f"Designed by: {self.name}\n"
        header += f"Date: {datetime.now().strftime('%d/%m/%Y')}\n\n"
        return header
    
    def generate_power_supply(self):
        power_supply = "Power Supply:\n\n"
        power_supply += "   - Main Power Source:\n"
        power_supply += f"       {self.get_random_color()} flux capacitor\n"
        power_supply += "   - Backup Power Source:\n"
        power_supply += "       Mr. Fusion\n\n"
        return power_supply
    
    def generate_time_circuits(self):
        time_circuits = "Time Circuits:\n\n"
        time_circuits += "   - Primary Interface:\n"
        time_circuits += "       Temporal Keypad\n"
        time_circuits += "   - Destination Inputs:\n"
        time_circuits += "       - Date\n"
        time_circuits += "       - Time\n"
        time_circuits += "   - Time Destination Display:\n"
        time_circuits += "       Digital Display\n"
        time_circuits += "   - Flux Capacitor Stabilizer:\n"
        time_circuits += "       Micro-Time Displacement Oscillator\n\n"
        return time_circuits
    
    def generate_flux_capacitor(self):
        flux_capacitor = "Flux Capacitor:\n\n"
        flux_capacitor += "   - Main Component:\n"
        flux_capacitor += "       Flux Capacitor Module\n"
        flux_capacitor += "   - Flux Energy Source:\n"
        flux_capacitor += "       High-Voltage Plutonium Chamber\n"
        flux_capacitor += "   - Flux Energy Regulator:\n"
        flux_capacitor += "       Time-Variable Magnetic Field Stabilizer\n"
        flux_capacitor += "   - Flux Energy Conversion:\n"
        flux_capacitor += "       Einstein-Rosen Bridge\n\n"
        return flux_capacitor
    
    def generate_dimensional_field_generator(self):
        dimensional_field = "Dimensional Field Generator:\n\n"
        dimensional_field += "   - Field Generation Device:\n"
        dimensional_field += "       Miniaturized Wormhole Generator\n"
        dimensional_field += "   - Field Strength Control:\n"
        dimensional_field += "       Quantum-Field Flux Control Valve\n"
        dimensional_field += "   - Field Structure Stabilizer:\n"
        dimensional_field += "       Gravitational Anomaly Compensators\n"
        dimensional_field += "   - Field Parameters Configuration:\n"
        dimensional_field += "       Atomic Waveform Harmonizer\n\n"
        return dimensional_field
    
    def generate_housing(self):
        housing = "Housing:\n\n"
        housing += f"   - Chassis Color: {self.get_random_color()}\n"
        housing += "   - Exterior Material:\n"
        housing += "       Light-Weight Graphene Composite\n"
        housing += "   - Interior Insulation:\n"
        housing += "       Temporal Energy Absorbers\n"
        housing += "   - Structural Integrity Enhancements:\n"
        housing += "       Reinforced Neutronium Alloy\n\n"
        return housing
    
    def generate_controls(self):
        controls = "Controls:\n\n"
        controls += "- Time Machine Operations Console:\n"
        controls += "   - Temporal Keypad\n"
        controls += "   - Data Analyzer\n"
        controls += "   - Temporal Flux Emitter Control\n"
        controls += "   - Chronological Mapping System\n"
        controls += "   - Alphanumeric Keyboard\n"
        controls += "   - Status Display Panel\n"
        controls += "   - Navigation Control Lever\n\n"
        return controls
    
    def generate_ancillary_systems(self):
        ancillary_systems = "Ancillary Systems:\n\n"
        ancillary_systems += "- Temporal Tactical Defense System:\n"
        ancillary_systems += "   - Temporal Force Field Emitter\n"
        ancillary_systems += "   - Chrono-Chaff Dispenser\n"
        ancillary_systems += "   - Temporally-Displaced Projectile Launcher\n"
        ancillary_systems += "   - Temporal Disruptor\n"
        ancillary_systems += "   - Phase Shifting Cloaking Device\n\n"
        return ancillary_systems
    
    def generate_fuel_system(self):
        fuel_system = "Fuel System:\n\n"
        fuel_system += "   - Fuel Type:\n"
        fuel_system += "       Plutonium (P-238)\n"
        fuel_system += "   - Fuel Container:\n"
        fuel_system += "       Plutonium Chamber\n"
        fuel_system += "   - Fuel Capacity:\n"
        fuel_system += "       1.21 Gigawatts\n\n"
        return fuel_system
    
    def generate_navigation_system(self):
        navigation_system = "Navigation System:\n\n"
        navigation_system += "   - Location Acquisition Methods:\n"
        navigation_system += "       - GPS Coordinates\n"
        navigation_system += "       - Temporal Spatial Temporizer\n"
        navigation_system += "   - Destination Guidance:\n"
        navigation_system += "       Heads-Up Holographic Display\n"
        navigation_system += "   - Time Machine Position Monitoring:\n"
        navigation_system += "       Time-Space Differential Synchronizer\n\n"
        return navigation_system
    
    def generate_protective_systems(self):
        protective_systems = "Protective Systems:\n\n"
        protective_systems += "   - Temporal Shields:\n"
        protective_systems += "       - Chrono-Displacement Shields\n"
        protective_systems += "       - Temporal Field Diffusers\n"
        protective_systems += "   - Time Machine Cloaking System:\n"
        protective_systems += "       - Optical Camouflage\n"
        protective_systems += "   - Anti-Time Paradox Safety Measures:\n"
        protective_systems += "       - Temporal Paradox Detector\n"
        protective_systems += "       - Temporal Flux Adjuster\n\n"
        return protective_systems
    
    def generate_finish(self):
        finish = f"Thank you for using the {self.name} Time Machine AI.\n"
        finish += "Please note that this is a fictional system and cannot be built.\n"
        finish += "This schematic is for entertainment purposes only.\n"
        return finish
    
    def get_random_color(self):
        return random.choice(self.colors)

# A test run of the TimeMachineAI class
if __name__ == "__main__":
    ai = TimeMachineAI("TimeMaster 9000")
    schematics = ai.create_schematics()
    print(schematics)