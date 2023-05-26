import numpy as np;
def calculate_pressure_drop(flow_rate, pipe_diameter, pipe_length, fluid_density, pipe_roughness, fluid_viscosity):
    # Calculate Reynolds number
    reynolds_number = (4 * flow_rate) / (pipe_diameter * fluid_viscosity)
    
    # Calculate friction factor using the Colebrook-White equation for turbulent flow
    relative_roughness = pipe_roughness / pipe_diameter
    epsilon = 0.0001  # A small value to check for convergence
    f = 0.02  # Initial guess for friction factor
    while True:
        f_prev = f
        numerator = (-2 * np.log10((relative_roughness / (3.7 * pipe_diameter)) + (2.51 / (reynolds_number * np.sqrt(f)))))
        denominator = (-2 * np.log10((relative_roughness / (3.7 * pipe_diameter)) + (2.51 / (reynolds_number * np.sqrt(f_prev)))))

        f = f_prev - (numerator - denominator)
        if abs(f - f_prev) < epsilon:
            break
    
    # Calculate pressure drop using the Darcy-Weisbach equation
    pressure_drop = (f * (pipe_length / pipe_diameter) * (fluid_density * (flow_rate ** 2))) / (2 * pipe_diameter)
    
    return pressure_drop

