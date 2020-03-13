# MapInfo
import pantherine as purr
import statistics as stats
import math

class MapInfo(object):
    
    DIR = ""
    nodes = []
    edges = []
    centroid = (float(),float())
    xMax = float()
    xMin = float()
    yMax = float()
    yMin = float()
    
    def __init__(self,DIR):
        self.DIR = DIR
        self.edges = purr.readXMLtag(purr.mrf(DIR,r"*.edg.xml"),"edge")
        self.nodes = purr.readXMLtag(purr.mrf(DIR,r"*.nod.xml"),"node")
        
        x = [float(node['x']) for node in self.nodes]
        y = [float(node['y']) for node in self.nodes]
        self.centroid = (stats.fmean(x),stats.fmean(y))
        self.xMax = max(x)
        self.xMin = min(x)
        self.yMax = max(y)
        self.yMin = min(y)
        return
    
    # Get an (x,y) position from the map when a normalized value
    # is input. 
    # @param normX = x value [0,1]
    # @param normY = y value [0,1]
    # trim = Cut off the x or y limit by this % [0,1] This makes sure that the point is someplace in the SUMO network
    def getPosition(self,normX,normY,trim=0.7):
        x = float()
        y = float()
        
        if normX == 0.5:
            x = self.centroid[0]
        elif normX < 0.5:
            x = self.xMin + (self.centroid[0] - self.xMin) * normX * trim
        else:
            x = self.centroid[0] + (self.xMax - self.centroid[0]) * normX * trim
            
        if normY == 0.5:
            y = self.centroid[1]
        elif normY < 0.5:
            y = self.yMin + (self.centroid[1] - self.yMin) * normY * trim
        else:
            y = self.centroid[1] + (self.yMax - self.centroid[1]) * normY * trim
            
        return (x,y)

