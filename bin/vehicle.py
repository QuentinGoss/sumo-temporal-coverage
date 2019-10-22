# vehicle.py
# Author: Quentin Goss
# Last Modified: 10/17/1995
import random
import env
import networkx as nx
import nxops
import pantherine as purr
import preprocess

# Adds a vehicle to the simulation
# @param traci = traci object
def add(traci):
    # Vehicle ID
    vid = "veh%d" % (env.veh_id_counter)
    env.veh_id_counter += 1
    
    # Selected a path. It must be have a conenction between spawn and sink
    ntrys = 0
    while True:
        # Pick a random spawn and sink edge
        spawn_edge = random.choice(env.spawn_edge)
        sink_edge = random.choice(env.sink_edge)
        
        # Determine the shortest path
        try:
            shortest_path = nx.dijkstra_path(env.nx,spawn_edge['from'],sink_edge['to'])
            break
        except nx.NetworkXNoPath:
            ntrys += 1
            print("%s: Cannont create a path between %s and %s... Trying again (%d)." % (vid,spawn_edge['from'],sink_edge['to'],ntrys))
        continue
        
    # At this point, it is assumed that the path is connected
    # Now the weight of the path and the edge eids of the path is determined
    shortest_path_weight, shortest_path_eids = nxops.path_info(env.nx,shortest_path)
    
    # display the spawn and sink destions
    spawn_node,sink_node = purr.flattenlist(purr.batchfilterdicts(env.nodes,'id',[shortest_path[0],shortest_path[-1]]))
    spawn_point = (float(spawn_node['x']),float(spawn_node['y']))
    sink_point = (float(sink_node['x']),float(sink_node['y']))
    preprocess.add_radius_polygon(traci,spawn_point,20,(0,255,255))
    preprocess.add_radius_polygon(traci,sink_point,20,(0,255,255))
    
    # Find the optimal target point to visit
    path = nxops.naive_target_selection(env.nx,shortest_path,env.target_nodes)
    
    # Create a route with the path eids
    rid = "route%d" % (env.route_id_counter)
    env.route_id_counter += 1
    traci.route.add(rid,path['path_eids'])
    
    # Add a vehicle
    traci.vehicle.add(vid,rid)
    
    # Determine the edge immediately after the node
    target_node_index = path['path_nids'].index(path['target_node']['id'])
    target_eid = path['path_eids'][target_node_index]
    
    # Create the vehicle dictionary
    veh = {
        "id":vid,
        "source":spawn_node['id'],
        "destination":sink_node['id'],
        "shortest path length":shortest_path_weight,
        "diversion path length":path['weight'],
        "sample time":None,
        "target nid":path['target_node']['id'],
        "target eid":target_eid,
        "path":path
    }
    env.vehicles.append(veh)
    return

# Checks if a vehicle has reached it's target
# @param traci = traci object
# @param string vid = vehicle ID
# @return True if vehicle is on it's target edge
def is_veh_at_target(traci,vid):
    index = int(vid[3:])
    if env.vehicles[index]['target eid'] == traci.vehicle.getRoadID(vid):
        return True
    return False

# Take a sample
# @param string vid = vehicle ID
# @param int n_step = Current timestep
def sample(vid,n_step):
    index = int(vid[3:])
    # Sample only once
    if not env.vehicles[index]['sample time'] == None:
        return
    # Record time
    env.vehicles[index]['sample time'] = n_step
    # Track the sample time on the target too
    tid = env.vehicles[index]['target nid']
    for itar in range(0,len(env.targets)):
        if env.targets[itar]['id'] == tid:
            env.targets[itar]['sampling times'][index] = n_step
            # ~ print("\n%s: Sample taken at %s!" % (vid,tid))
            break    
    return

# Writes the result of simulation to csv
def csv():
    print("Writing vehicles.csv...",end='')
    with open("%s/vehicles.csv" % (env.out_dir),'w') as f:
        f.write("id,source,destination,shortest path length,diversion path length,sample time,target id\n")
        for veh in env.vehicles:
            f.write("%s,%s,%s,%.3f,%.3f,%d,%s\n" % (veh['id'],veh['source'],veh['destination'],veh['shortest path length'],veh['diversion path length'], veh['sample time'], veh['target nid']))
            continue
    print("Complete!")
    return
