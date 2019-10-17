# preprocess.py
# Author: Quentin Goss
# Preprocessing steps are kept in this file
import env
import pantherine as purr

# Finds valid edges around an point
# @param (float,float) point = (x,y) point
# @param float radius = radius around point
def get_valid_edges_from_point(point,radius):
    print("Finding valid edges for point",point,"and radius",radius)
    x,y = point
    
    # Find the nodes that are within the radius
    nod_xml = purr.mrf(env.options.map_dir,r'*.nod.xml')
    nodes_all = purr.readXMLtag(nod_xml,'node')
    nodes_valid = []
    for node in nodes_all:
        if abs(x - float(node['x'])) <= radius and abs(y - float(node['y'])) <= radius:
            nodes_valid.append(node)
        continue
    nodes_valid_ids = [node['id'] for node in nodes_valid]
    
    # Now that we know the nodes, we can pick out valid edges that the node begins at
    edg_xml = purr.mrf(env.options.map_dir,r'*.edg.xml')
    edges_all = purr.readXMLtag(edg_xml,'edge')
    edges_filtered = purr.batchfilterdicts(edges_all,'from',nodes_valid_ids,show_progress=True)
    edges_filtered = purr.flattenlist(edges_filtered)
    edges_valid_ids = []
    for edge in edges_filtered:
        if not ':' in edge['id']:
            edges_valid_ids.append(edge['id'])
    
    print("Found %d edge candidates." % (len(edges_valid_ids)))
    
    return edges_valid_ids
    
# Creates a polygon for visualization of spawn/sink radius
def add_radius_polygon(traci,point,radius,color):
    x,y = point
    pid = 'poly%d' % (len(traci.polygon.getIDList())+1)
    shape = [(x-radius,y-radius),(x-radius,y+radius),(x+radius,y+radius),(x+radius,y-radius)]
    traci.polygon.add(pid,shape,color,fill=True,layer=1)
    return

