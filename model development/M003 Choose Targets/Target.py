# Target.py
from POI import POI

class Target(POI):
    def __init__(self,index,xNorm,yNorm,mapInfo,traci):
        super().__init__(index,xNorm,yNorm,mapInfo,traci)
        return
