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
    
    def generate_section(self, title, content):
        section = f"{title}:\n\n"
        section += content
        section += "\n"
        return section
    
    def generate_power_supply(self):
        power_supply = self.generate_section("Power Supply", 
            "   - Main Power Source:\n"
            f"       {self.get_random_color()} flux capacitor\n"
            "   - Backup Power Source:\n"
            "       Mr. Fusion"
        )
        return power_supply
    
    def generate_time_circuits(self):
        time_circuits = self.generate_section("Time Circuits",
            "   - Primary Interface:\n"
            "       Temporal Keypad\n"
            "   - Destination Inputs:\n"
            "       - Date\n"
            "       - Time\n"
            "   - Time Destination Display:\n"
            "       Digital Display\n"
            "   - Flux Capacitor Stabilizer:\n"
            "       Micro-Time Displacement Oscillator"
        )
        return time_circuits
    
    def generate_flux_capacitor(self):
        flux_capacitor = self.generate_section("Flux Capacitor",
            "   - Main Component:\n"
            "       Flux Capacitor Module\n"
            "   - Flux Energy Source:\n"
            "       High-Voltage Plutonium Chamber\n"
            "   - Flux Energy Regulator:\n"
            "       Time-Variable Magnetic Field Stabilizer\n"
            "   - Flux Energy Conversion:\n"
            "       Einstein-Rosen Bridge"
        )
        return flux_capacitor
    
    def generate_dimensional_field_generator(self):
        dimensional_field = self.generate_section("Dimensional Field Generator",
            "   - Field Generation Device:\n"
            "       Miniaturized Wormhole Generator\n"
            "   - Field Strength Control:\n"
            "       Quantum-Field Flux Control Valve\n"
            "   - Field Structure Stabilizer:\n"
            "       Gravitational Anomaly Compensators\n"
            "   - Field Parameters Configuration:\n"
            "       Atomic Waveform Harmonizer"
        )
        return dimensional_field
    
    def generate_housing(self):
        housing = self.generate_section("Housing",
            f"   - Chassis Color: {self.get_random_color()}\n"
            "   - Exterior Material:\n"
            "       Light-Weight Graphene Composite\n"
            "   - Interior Insulation:\n"
            "       Temporal Energy Absorbers\n"
            "   - Structural Integrity Enhancements:\n"
            "       Reinforced Neutronium Alloy"
        )
        return housing
    
    def generate_controls(self):
        controls = self.generate_section("Controls",
            "- Time Machine Operations Console:\n"
            "   - Temporal Keypad\n"
            "   - Data Analyzer\n"
            "   - Temporal Flux Emitter Control\n"
            "   - Chronological Mapping System\n"
            "   - Alphanumeric Keyboard\n"
            "   - Status Display Panel\n"
            "   - Navigation Control Lever"
        )
        return controls
    
    def generate_ancillary_systems(self):
        ancillary_systems = self.generate_section("Ancillary Systems",
            "- Temporal Tactical Defense System:\n"
            "   - Temporal Force Field Emitter\n"
            "   - Chrono-Chaff Dispenser\n"
            "   - Temporally-Displaced Projectile Launcher\n"
            "   - Temporal Disruptor\n"
            "   - Phase Shifting Cloaking Device"
        )
        return ancillary_systems
    
    def generate_fuel_system(self):
        fuel_system = self.generate_section("Fuel System",
            "   - Fuel Type:\n"
            "       Plutonium (P-238)\n"
            "   - Fuel Container:\n"
            "       Plutonium Chamber\n"
            "   - Fuel Capacity:\n"
            "       1.21 Gigawatts"
        )
        return fuel_system
    
    def generate_navigation_system(self):
        navigation_system = self.generate_section("Navigation System",
            "   - Location Acquisition Methods:\n"
            "       - GPS Coordinates\n"
            "       - Temporal Spatial Temporizer\n"
            "   - Destination Guidance:\n"
            "       Heads-Up Holographic Display\n"
            "   - Time Machine Position Monitoring:\n"
            "       Time-Space Differential Synchronizer"
        )
        return navigation_system
    
    def generate_protective_systems(self):
        protective_systems = self.generate_section("Protective Systems",
            "   - Temporal Shields:\n"
            "       - Chrono-Displacement Shields\n"
            "       - Temporal Field Diffusers\n"
            "   - Time Machine Cloaking System:\n"
            "       - Optical Camouflage\n"
            "   - Anti-Time Paradox Safety Measures:\n"
            "       - Temporal Paradox Detector\n"
            "       - Temporal Flux Adjuster"
        )
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