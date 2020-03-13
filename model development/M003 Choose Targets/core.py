import env
# ~ import vehicle
import os
import pantherine as purr
# ~ import preprocess
# ~ import target
# ~ import nxops
# ~ import spm
# ~ import distance
# ~ import point
# ~ import systematicSim2 as ss2
from SS2Wrapper import SS2Wrapper
from MapInfo import MapInfo
from Target import Target
from Source import Source
from Destination import Destination
from Vehicle import Vehicle

###############################
# Initilize anything that needs to happen at step 0 here.
###############################
def initialize(traci):
    # ~ os.system("cls")
    print("Initializing...")
    
    # Traci
    env.traci = traci
    
    # MapInfo
    env.mapInfo = MapInfo(env.options.map_dir)
    
    # ss2Wrapper
    N = 10; M = 5
    env.ss2Wrapper = SS2Wrapper(N,M)
    
    # src, dst, and tar POIs
    src,dst,tar = env.ss2Wrapper.getLocalizedPlacementNorm()
    env.src = [Source(i,xy[0],xy[1],env.mapInfo,traci) for i,xy in enumerate(src)]
    env.dst = [Source(i,xy[0],xy[1],env.mapInfo,traci) for i,xy in enumerate(dst)]
    env.tar = [Source(i,xy[0],xy[1],env.mapInfo,traci) for i,xy in enumerate(tar)]
    
    r = traci.simulation.findRoute(env.src[0].eid,env.dst[0].eid)
    # ~ print(r.edges)
    
    env.vehicles = [Vehicle(i,env.src[i],env.dst[i]) for i,s in enumerate(env.src)]
    env.vehicles[0].add(traci)
    # ~ [veh.add(traci) for veh in env.vehicles]
    purr.pause()
    
    
    # ~ preprocess.initialize_nx()
    # ~ preprocess.initialize_edges_and_nodes()
    
    
    # ~ point.validate()
    # ~ vehicle.initialize()
    # ~ target.initialize(traci)
    # ~ spm.generate_tar2dest()
    # ~ env.dist = distance.distance()
    
    # ~ n = 0; total = env.veh_exists_max;
    # ~ for i in range(0,env.veh_exists_max):
        # ~ vehicle.add()
        # ~ n += 1; purr.update(n,total,msg="Adding first %d vehicles " % (env.veh_exists_max))
        # ~ continue
    # ~ print()
        
    # ~ vehicle.update()
    # ~ spm.update_veh2tar()
    # ~ env.nash_assigner = ss2.nashAssigner(N=len(env.vPd),M=len(env.tP),R=env.R,tau=env.tau,dist=env.dist)
    # ~ if env.method == "greedy":
        # ~ vehicle.set_route(env.nash_assigner.greedyAssignments())
    # ~ else:
        # ~ vehicle.set_route(env.nash_assigner.getAssignments())
        
    # ~ env.update_vehicle_info = True

    print("Initialization complete!")
    return
# end def intialize


###############################
# Anything that hvppens within the TraCI control loop goes here.
# One pass of the loop
    # ~ preprocess.initialize_edge == 1 timestep.
# Return False to finalize the simulation
###############################
def timestep(traci,n_step):
    return False
    # ~ # Take samples if neccesary
    # ~ for vid in traci.vehicle.getIDList():
        # ~ if vehicle.is_veh_at_target(vid):
            # ~ vehicle.sample(vid,n_step)
    
    # ~ if env.method == "smart" and env.recalculate_nash:
        # ~ env.recalculate_nash = False
        # ~ vehicle.update()
        # ~ spm.update_veh2tar()
        # ~ vehicle.set_route(env.nash_assigner.getAssignments())
    
    # ~ # End of Simulation condition
    # ~ if (traci.vehicle.getIDCount() <= 0) and (env.veh_id_counter >= (env.veh_total - 1)):
        # ~ print("All vehicles have arrived at their destinations.")
        # ~ return False
        
    # ~ # Add another vehicle condition
    # ~ elif traci.vehicle.getIDCount() < env.veh_exists_max and env.veh_id_counter < env.veh_total:
        # ~ print("\nAdding another vehicle.",env.veh_id_counter, env.veh_total)
        # ~ vehicle.add()
    return True
# end timestep

###############################
# Finalize the Simulation
###############################
def finalize():
    # ~ if os.path.exists(env.out_dir):
        # ~ purr.deldir(env.out_dir)
    # ~ os.mkdir(env.out_dir)
    # ~ vehicle.csv()
    # ~ vehicle.out_pretty()
    # ~ target.csv()
    # ~ target.out_pretty()
    
    # ~ if env.method == "greedy":
        # ~ purr.save(env.nA_greedy_file,env.nash_assigner)
    # ~ else:
        # ~ purr.save(env.nA_smart_file,env.nash_assigner)
    return
# End finalize
