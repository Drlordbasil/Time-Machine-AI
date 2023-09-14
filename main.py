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

# Let's now improve the code:
# 1. Move the print statements into a separate function for better readability
# 2. Add input validation for distance and velocity inputs
# 3. Use f-strings for displaying input and output values
# 4. Use properties for calculated values


class TimeMachineCalculator:
    def __init__(self, distance, velocity):
        self._distance = distance
        self._velocity = velocity

    @property
    def distance(self):
        return self._distance

    @property
    def velocity(self):
        return self._velocity

    @property
    def time(self):
        return self.distance / self.velocity

    @property
    def energy(self):
        return (self.velocity ** 2) / 2

    @property
    def acceleration(self):
        return self.velocity / self.time

    @property
    def force(self):
        return self.energy / self.distance

    @property
    def power(self):
        return self.force * self.velocity

    @property
    def work_done(self):
        return self.force * self.distance

    def calculate_momentum(self, mass):
        return mass * self.velocity

    def display_results(self, mass=None):
        print("Calculation Results:")
        print(f"Time: {self.time} seconds")
        print(f"Energy: {self.energy} joules")
        print(f"Acceleration: {self.acceleration} m/s^2")
        print(f"Force: {self.force} newtons")
        print(f"Power: {self.power} watts")
        print(f"Work Done: {self.work_done} joules")
        if mass is not None:
            print(f"Momentum: {self.calculate_momentum(mass)} kg*m/s")


def get_distance():
    while True:
        try:
            distance = float(input("Distance (in meters): "))
            if distance > 0:
                return distance
            else:
                print("Distance must be greater than 0!")
        except ValueError:
            print("Invalid input! Please enter a number for distance.")


def get_velocity():
    while True:
        try:
            velocity = float(input("Velocity (in meters per second): "))
            if velocity > 0:
                return velocity
            else:
                print("Velocity must be greater than 0!")
        except ValueError:
            print("Invalid input! Please enter a number for velocity.")


def main():
    print("Welcome to Time-Machine-AI")
    print("Please provide the following information:")

    distance = get_distance()
    velocity = get_velocity()

    calculator = TimeMachineCalculator(distance, velocity)
    calculator.display_results()


if __name__ == "__main__":
    main()