# Improved Code:

import math

class TimeMachineCalculator:
    def __init__(self, distance, velocity):
        if distance <= 0 or velocity <= 0:
            raise ValueError("Distance and velocity must be greater than 0!")
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
        return self.calculate_time()

    @property
    def energy(self):
        return self.calculate_energy()

    @property
    def acceleration(self):
        return self.calculate_acceleration()

    @property
    def force(self):
        return self.calculate_force()

    @property
    def power(self):
        return self.calculate_power()

    @property
    def work_done(self):
        return self.calculate_work_done()

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


class TimeMachineAI:
    @staticmethod
    def display_results(time_machine):
        print("Calculation Results:")
        print(f"Time: {time_machine.time} seconds")
        print(f"Energy: {time_machine.energy} joules")
        print(f"Acceleration: {time_machine.acceleration} m/s^2")
        print(f"Force: {time_machine.force} newtons")
        print(f"Power: {time_machine.power} watts")
        print(f"Work Done: {time_machine.work_done} joules")

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def main():
        print("Welcome to Time-Machine-AI")
        print("Please provide the following information:")

        distance = TimeMachineAI.get_distance()
        velocity = TimeMachineAI.get_velocity()

        calculator = TimeMachineCalculator(distance, velocity)
        TimeMachineAI.display_results(calculator)


if __name__ == "__main__":
    TimeMachineAI.main()