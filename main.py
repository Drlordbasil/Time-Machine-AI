import math

def calculate_energy(mass, velocity):
    energy = mass * velocity**2
    return energy

def calculate_time_dilation(acceleration, time):
    velocity = acceleration * time
    time_dilation = math.sqrt(1 - (velocity**2 / (299792458**2)))
    return time_dilation

def calculate_coordinate(time, distance):
    coordinate = distance * math.exp(-time)
    return coordinate

def calculate_time_travel(time_dilation, time):
    time_travel = time / math.sqrt(1 - time_dilation**2)
    return time_travel

def calculate_schematic(length, width, height):
    volume = length * width * height
    surface_area = 2 * (length * width + length * height + width * height)
    return volume, surface_area

def print_schematic(schematic):
    volume, surface_area = schematic
    print(f"Time Machine Schematic:")
    print(f"Volume: {volume} cubic units")
    print(f"Surface Area: {surface_area} square units")

def main():
    print("Welcome to the Time Machine AI!")
    print("Please enter the following details:")

    mass = float(input("Mass of Time Machine (in kg): "))
    velocity = float(input("Velocity of Time Machine (in m/s): "))

    energy = calculate_energy(mass, velocity)
    print(f"Energy required for Time Machine: {energy} J")

    acceleration = float(input("Acceleration of Time Machine (in m/s^2): "))
    time = float(input("Time (in s): "))

    time_dilation = calculate_time_dilation(acceleration, time)
    print(f"Time Dilation: {time_dilation}")

    distance = float(input("Distance (in m): "))

    coordinate = calculate_coordinate(time, distance)
    print(f"Coordinate in Time Machine: {coordinate}")

    time_travel = calculate_time_travel(time_dilation, time)
    print(f"Time Travel: {time_travel} s")

    length = float(input("Length of Time Machine (in units): "))
    width = float(input("Width of Time Machine (in units): "))
    height = float(input("Height of Time Machine (in units): "))

    schematic = calculate_schematic(length, width, height)
    print_schematic(schematic)

if __name__ == "__main__":
    main()