import env
import vehicle
import os
import pantherine as purr
import preprocess

###############################
# Initilize anything that needs to happen at step 0 here.
###############################
def initialize(traci):
    os.system("cls")
    print("Initializing...")
    
    print("Finding spawn edge candidates.")
    try:
        spawn_edge_ids = purr.load('temp/spawns.bin')
    except FileNotFoundError:
        spawn_edge_ids = preprocess.get_valid_edges_from_point(env.point_spawn,env.radius_spawn_sink)
        purr.save('temp/spawns.bin',spawn_edge_ids)
    preprocess.add_radius_polygon(traci,env.point_spawn,env.radius_spawn_sink,(0,255,0))
    
    print("Finding sink edge candidates.")
    try:
        sink_edge_ids = purr.load('temp/sinks.bin')
    except FileNotFoundError:
        sink_edge_ids = preprocess.get_valid_edges_from_point(env.point_sink,env.radius_spawn_sink)
        purr.save('temp/sinks.bin',sink_edge_ids)
    preprocess.add_radius_polygon(traci,env.point_sink,env.radius_spawn_sink,(255,0,0))
    
    purr.pause()
    
    # ~ for i in range(0,env.veh_exists_max):
        # ~ vehicle.add(traci)
    print("Initialization complete!")
    purr.pause()
    return
# end def intialize


###############################
# Anything that happens within the TraCI control loop goes here.
# One pass of the loop == 1 timestep.
# Return False to finalize the simulation
###############################
def timestep(traci,n_step):
    
    return True
# end timestep

###############################
# Finalize the Simulation
###############################
def finalize():
    
    return
# End finalize
