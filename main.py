import math

class TimeMachineCalculator:
    def __init__(self, distance, velocity):
        self.distance = distance
        self.velocity = velocity

    def calculate_time(self):
        time = self.distance / self.velocity
        return time

    def calculate_energy(self):
        energy = (self.velocity**2) / 2
        return energy

    def calculate_acceleration(self):
        acceleration = self.velocity / self.calculate_time()
        return acceleration

    def calculate_force(self):
        force = self.calculate_energy() / self.distance
        return force

    def calculate_power(self):
        power = self.calculate_force() * self.velocity
        return power

    def calculate_work_done(self):
        work_done = self.calculate_force() * self.distance
        return work_done

    def calculate_momentum(self, mass):
        momentum = mass * self.velocity
        return momentum

    def display_results(self, mass=None):
        print("Calculation Results:")
        print(f"Time: {self.calculate_time()} seconds")
        print(f"Energy: {self.calculate_energy()} joules")
        print(f"Acceleration: {self.calculate_acceleration()} m/s^2")
        print(f"Force: {self.calculate_force()} newtons")
        print(f"Power: {self.calculate_power()} watts")
        print(f"Work Done: {self.calculate_work_done()} joules")
        if mass is not None:
            print(f"Momentum: {self.calculate_momentum(mass)} kg*m/s")

def main():
    print("Welcome to Time-Machine-AI")
    print("Please provide the following information:")

    distance = float(input("Distance (in meters): "))
    velocity = float(input("Velocity (in meters per second): "))

    calculator = TimeMachineCalculator(distance, velocity)
    calculator.display_results()

if __name__ == "__main__":
    main()