# POI.py

class POI(object):
    
    index = -1
    xNorm = float()
    yNorm = float()
    xSumo = float()
    ySumo = float()
    eid = str()
    distance = float()
    lane = int()
    
    def __init__(self,index,xNorm,yNorm,mapInfo,traci):
        self.index = index
        self.xNorm = xNorm
        self.yNorm = yNorm
        self.xSumo,self.ySumo = mapInfo.getPosition(xNorm,yNorm)
        self.eid,self.distance,self.lane = traci.simulation.convertRoad(self.xSumo,self.ySumo)
        return
    
    def toDict(self):
        d = {
            "index" : self.index,
            "xNorm" : self.xNorm,
            "yNorm" : self.yNorm,
            "xSumo" : self.xSumo,
            "ySumo" : self.ySumo,
            "eid" : self.eid,
            "distance" : self.distance,
            "lane" : self.lane
        }
        return d
