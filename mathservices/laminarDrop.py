import math

def calculate_pressure_drop(viscosity, length, diameter, flow_rate):
    # Convert diameter to meters
    diameter_m = diameter / 1000.0

    # Calculate the cross-sectional area of the pipe
    area = math.pi * (diameter_m / 2) ** 2

    # Calculate the Reynolds number
    reynolds_number = (4 * flow_rate) / (math.pi * viscosity * diameter_m)

    # Calculate the pressure drop
    pressure_drop = (128 * viscosity * length * flow_rate) / (math.pi * diameter_m ** 4)

    return pressure_drop