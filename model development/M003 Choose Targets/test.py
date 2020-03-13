from MapInfo import MapInfo

def main():
    mapDir = "../../TAPASCologne-0.32.0"
    mapInfo = MapInfo(mapDir)
    print(mapInfo.getPosition(0.5,0.5))
    return
    
if __name__ == "__main__":
    main()
