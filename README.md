# pressureDrop

open terminal and run python main.py

For single element pressure drop, just use end point pressureDrop.
For a collection of pressure drops, use pressureArray.

For <url>/pressureDrop, format body required is something like this:
  
    {
      "flow_rate" : 0.3,
      "pipe_diameter" : 0.05,  
      "pipe_length" : 10,  
      "fluid_density" : 1000,  
      "pipe_roughness" : 0.001,  
      "fluid_viscosity" : 0.0025
    }

  Response Output for <url>/pressureDrop:
  
    {
      "result in Pa": 3600.0
    }
  
  
For <url>/pressureArray, format body required is something like this:
  
    {
      "content":[
          {
              "flow_rate" : 0.3,
              "pipe_diameter" : 0.05,  
              "pipe_length" : 10,  
              "fluid_density" : 1000,  
              "pipe_roughness" : 0.001,  
              "fluid_viscosity" : 0.0025

          },
          {
              "flow_rate" : 0.3,
              "pipe_diameter" : 0.05,  
              "pipe_length" : 10,  
              "fluid_density" : 100,  
              "pipe_roughness" : 0.001,  
              "fluid_viscosity" : 0.0025
          }
      ]

    }
  
  Response Output <url>/pressureArray:
  
    {
      "result in Pa": [
          3600.0,
          360.0
      ]
    }
