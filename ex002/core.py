import env
import vehicle
import os
import pantherine as purr
import preprocess
import target
import nxops
import spm

###############################
# Initilize anything that needs to happen at step 0 here.
###############################
def initialize(traci):
    os.system("cls")
    print("Initializing...")
    
    preprocess.initialize_nx()
    preprocess.initialize_edges_for_spawns_and_sinks(traci)
    target.initialize(traci)
    env.traci = traci
    vehicle.initialize()
    spm.generate_tar2dest()
    
    n = 0; total = env.veh_exists_max;
    for i in range(0,env.veh_exists_max):
        vehicle.add()
        n += 1; purr.update(n,total,msg="Adding first %d vehicles " % (env.veh_exists_max))
        continue
        
    env.update_vehicle_info = True
        
    print("Initialization complete!")
    return
# end def intialize


###############################
# Anything that happens within the TraCI control loop goes here.
# One pass of the loop == 1 timestep.
# Return False to finalize the simulation
###############################
def timestep(traci,n_step):
    # Update vehicle info if needed
    if (env.update_vehicle_info):
        vehicle.update()
        spm.update_veh2tar()
        purr.pause()
    
    # End of Simulation condition
    if (traci.vehicle.getIDCount() <= 0) and (env.veh_id_counter >= (env.veh_total - 1)):
        print("All vehicles have arrived at their destinations.")
        return False
        
    # Add another vehicle condition
    elif traci.vehicle.getIDCount() < env.veh_exists_max and env.veh_id_counter < env.veh_total:
        print("\nAdding another vehicle.",env.veh_id_counter, env.veh_total)
        vehicle.add()
    return True
# end timestep

###############################
# Finalize the Simulation
###############################
def finalize():
    return
# End finalize
