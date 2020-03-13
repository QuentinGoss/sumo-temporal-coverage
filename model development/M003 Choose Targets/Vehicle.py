# Vehicle.py

class Vehicle(object):
    index = int()
    vid = str()
    src = None
    dst = None
    eid = str()
    def __init__(self,index,src,dst):
        self.index = index
        self.src = src
        self.dst = dst
        self.vid = "veh-%d" % (index)
        return
        
    def add(self,traci):
        stage = traci.simulation.findRoute(self.src.eid,self.dst.eid)
        print(stage.edges)
        rid = "route-%d" % (traci.route.getIDCount())
        traci.route.add(rid,stage.edges)
        traci.vehicle.add(self.vid,rid)
        return
