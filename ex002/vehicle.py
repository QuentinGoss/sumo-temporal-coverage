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
def add():
    # Vehicle ID
    index = env.veh_id_counter
    env.veh_id_counter += 1
    vid = "veh%d" % (index)
    
    # Retrieve Route
    veh = env.vehicles[index]
    
    # Create a route with the path eids
    rid = "route%d" % (env.route_id_counter)
    env.route_id_counter += 1
    env.traci.route.add(rid,veh['shortest path']['eids'])
    
    # Add a vehicle
    env.traci.vehicle.add(vid,rid)
    
    # Add the destination node to list of sink nodes so it may be found later
    dest_node = purr.filterdicts(env.nodes,'id',veh['shortest path']['nids'][-1])[0]
    env.vehicles_dest.append(dest_node)
    return

# Inititalizes the shortests path of all vehicles
def initialize():
    env.vehicles = [None for iveh in range(env.veh_total)]
    total = len(env.vehicles)
    for i, x in enumerate(env.vehicles):
        veh = vehdict()
        veh['id'] = 'veh%d' % (i)
        veh['shortest path'] = random_shortest_path()
        env.vehicles[i] = veh
        purr.update(i+1,total,"Initializing Vehicles ")
    print()
    return

# Determines the spawn and sink node
# @return A random but valid shortest path
def random_shortest_path():
    # Selected a path. It must be have a conenction between spawn and sink
    ntrys = 0; shortest_path = {'weight':None,'nids':None,'eids':None}
    while True:
        # Pick a random spawn and sink edge
        spawn_edge = random.choice(env.spawn_edge)
        sink_edge = random.choice(env.sink_edge)
        
        # Determine the shortest path
        try:
            shortest_path['nids'] = nx.dijkstra_path(env.nx,spawn_edge['from'],sink_edge['to'])
            break
        except nx.NetworkXNoPath:
            ntrys += 1
            print("Cannont create a path between %s and %s... Trying again (%d)." % (spawn_edge['from'],sink_edge['to'],ntrys))
        continue
        
    # At this point, it is assumed that the path is connected
    # Now the weight of the path and the edge eids of the path is determined
    shortest_path['weight'], shortest_path['eids'] = nxops.path_info(env.nx,shortest_path['nids'])
    
    return shortest_path

# Updates vehicle position and situation
def update():
    env.update_vehicle_info = False
    
    # Clean out the old object 
    env.vehicles_active = []
    
    # Refill 
    for i,vid in enumerate(env.traci.vehicle.getIDList()):
        veh = dict()
            
        # Who am I?
        veh['id'] = vid
        
        # Where am I?
        veh['route index'] = env.traci.vehicle.getRouteIndex(veh['id'])
        
        # What is my route?
        veh['route id'] = env.traci.vehicle.getRouteID(veh['id'])
        
        # What is my sink node?
        veh['destination node'] = env.vehicles_dest[int(veh['id'][3:])]
        
        # How far along the edge am I (m)?
        veh['position on edge (m)'] = env.traci.vehicle.getLanePosition(veh['id'])
        
        # What edge am I on?
        eid = env.traci.vehicle.getRoadID(veh['id'])
        
        
        # Obtain the edge object. Here we can have two cases:
        #  1. veh is at an intersection
        #  2. veh is on an edg
        
        # Veh is within an intersection. Assume the start of the next edge with a position on edge (m) of zero.
        if ':' in eid:
            veh['route'] = env.traci.route.getEdges(veh['route id'])
            eid = veh['route'][veh['route index']+1]
            veh['current edge'] = purr.filterdicts(env.edges,'id',eid)[0]
            veh['position on edge (m)'] = 0.000001
        else:
            veh['current edge'] = purr.filterdicts(env.edges,'id',eid)[0]
            
        # How far am I along the edge (weight)
        veh['position on edge (s)'] = veh['position on edge (m)'] / float(veh['current edge']['speed'])
            
        # How much weight to the end of the edge?
        edge_candidates = env.nx.get_edge_data(veh['current edge']['from'],veh['current edge']['to'])
        for i in range(len(edge_candidates)):
            if veh['current edge']['id'] == edge_candidates[i]['id']:
                veh['weight remaining'] = edge_candidates[i]['weight'] - veh['position on edge (s)']
                break
            continue
            
        # How much weight is left for the shortest path?
        veh['short path weight'] = veh['weight remaining'] + nxops.path_info(env.nx,nx.dijkstra_path(env.nx,veh['current edge']['to'],veh['destination node']['id']))[0]

        env.vehicles_active.append(veh)
        continue
    return

def vehdict():
    veh = {
        'id':None,
        'shortest path':None
    }
    return veh
