from mathservices.pressureDrop import calculate_pressure_drop
from flask import request
def pressureController():
    data = request.json
    flow_rate = data['flow_rate'] # cubic meters per second
    pipe_diameter = data['pipe_diameter'] # meters
    pipe_length = data['pipe_length'] # meters
    fluid_density = data['fluid_density'] # kilograms per cubic meter
    pipe_roughness = data['pipe_roughness'] # meters
    fluid_viscosity = data['fluid_viscosity'] # Pascal-seconds
    
    pressure_drop = calculate_pressure_drop(flow_rate, pipe_diameter, pipe_length, fluid_density, pipe_roughness, fluid_viscosity)

    return pressure_drop

