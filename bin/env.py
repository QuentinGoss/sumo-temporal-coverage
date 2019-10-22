# env.py
options = None

# Vehicles
veh_total = None      # Number of vehicles to simulate
veh_exists_max = None # Number of vehicles that may exist at any point in time.
veh_id_counter = 0
vehicles = [] # List of tracked vehicles

# Routes
route_id_counter = 0

# Spawn and Sinks
point_spawn = None # (x.xx,y.yy)
point_sink = None  # (x.xx,y.yy)
radius_spawn_sink = None #
spawn_edges = None # [edge0,edge1,...,edgeN]
sink_edges = None  # [edge0,edge1,...,edgeN]

# Edge/Node dictionaries
edges = None # Edge dictionaries for every edge in the map
nodes = None # Node dictionaries for every node in the map

# Networkx graph
nx = None

# targets
target_nodes = None # [node0,node1,...,nodeN]
targets = [] # List of targets

# output directory
out_dir = None


