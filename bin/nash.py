# nash.py
# Author: Quentin Goss
import pantherine as purr
import env
import vehicle
import systematicSim as sysSim
import numpy as np
import nxops

# Recalculate the nash equation.
def recalculate():
    env.recalculate_nash = False
    print()
    
    print("Retrieving spatial vehicle data...",end='')
    st = purr.now()
    vehicle.update_nash()
    print("Complete after %.3fs" % (purr.elapsed(st)))
    
    print("Recalculating target assignments...",end='')
    st = purr.now()
    env.nash_assigner = sysSim.nashAssigner(N=len(env.vids_active),M=len(env.targets),R=200,tau=1,dist=env.dist)
    t = env.nash_assigner.getAssignments()
    print("Complete after %.3fs" % (purr.elapsed(st)))
    
    cDest = t[0] 
    utilities = t[1]
    #print target assignments 
    print('Assigining vehicles to new targets.')
    for x in range(env.nash_assigner.N):
        print('vehicle,target,utililty: (%d,%.0f,%.3f)'%(x,cDest[x],utilities[x]))
        
        veh = env.vehicles_active[x]
        path = dict()
        
        # Not worth the effort. Go home
        if np.isnan(cDest[x]):
            path['nids'] = nxops.dijkstra(env.nx,veh['current edge']['from'],veh['destination node']['id'])
            
        # Otherwise, go to the target
        else:
            tar = env.target_nodes[int(cDest[x])]
            path['nids'] = nxops.dijkstra(env.nx,veh['current edge']['from'],tar['id'])
        
        path['weight'] , path['eids'] = nxops.path_info(env.nx,path['nids'])
        
        # ~ rid = 'route%d' % (env.route_id_counter)
        # ~ env.route_id_counter += 1
        # ~ env.traci.route.add(rid,path['eids'])
        env.traci.vehicle.setRoute(veh['id'],path['eids'])
            
        continue
        
    print('Dijkstra: Calls=%d Time=%.3fs Avg=%.3fs' % (env.fs_dijkstra['calls'],env.fs_dijkstra['time'],env.fs_dijkstra['time']/env.fs_dijkstra['calls']))
    
    return
