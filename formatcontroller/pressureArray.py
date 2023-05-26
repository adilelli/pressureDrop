from mathservices.pressureDrop import calculate_pressure_drop
from flask import request
def pressureArrayController():
    data = request.json
    contentArray = data['content']
    arr = []
    for content in contentArray:
        flow_rate = content['flow_rate'] # cubic meters per second
        pipe_diameter = content['pipe_diameter'] # meters
        pipe_length = content['pipe_length'] # meters
        fluid_density = content['fluid_density'] # kilograms per cubic meter
        pipe_roughness = content['pipe_roughness'] # meters
        fluid_viscosity = content['fluid_viscosity'] # Pascal-seconds
        
        pressure_drop = calculate_pressure_drop(flow_rate, pipe_diameter, pipe_length, fluid_density, pipe_roughness, fluid_viscosity)
        arr.append(pressure_drop)

    return arr