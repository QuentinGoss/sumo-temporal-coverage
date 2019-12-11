# simSync.py
# Simulation Sychronizer

import pantherine as purr
import systematicSim2 as ss2

class SimulationSychronizer(object):
    def __init__(self):
        self.map_dir = "../london-seg4/data/"
        self.nodes = purr.readXMLtag(purr.mrf(self.map_dir,r'*.nod.xml'),'node')
        
        self.N = 100 # Vehicles
        self.M = 25  # Targets
        vPs, vPd = ss2.getLocalizedPlacement(self.N,self.M)
        return
    
    # Correlates a set of points to nodes in a sumo MAP
    # @param P = Numpy array of normalized points
    def correlateNormalPoints2SumoNodes(P):
        return
    
    # Adds two additional values to the node dictionaries:
    # normX and normY which are normalized X,Y values
    def normalizeNodes():
        return
    pass

def run():
    ss = SimulationSychronizer()

if __name__ == "__main__":
    run()
