import math


class TimeMachineCalculator:
    def __init__(self, distance, velocity):
        self.distance = distance
        self.velocity = velocity

    def calculate_time(self):
        return self.distance / self.velocity

    def calculate_energy(self):
        return (self.velocity ** 2) / 2

    def calculate_acceleration(self):
        return self.velocity / self.calculate_time()

    def calculate_force(self):
        return self.calculate_energy() / self.distance

    def calculate_power(self):
        return self.calculate_force() * self.velocity

    def calculate_work_done(self):
        return self.calculate_force() * self.distance

    def calculate_momentum(self, mass):
        return mass * self.velocity

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