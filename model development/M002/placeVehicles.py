import pantherine as purr
import systematicSim2 as ss2
import matplotlib.pyplot as plt

def main():
    src,dst,tar = getLocalizedPlacementNorm(N=30,M=5);
    plotGame(src,dst,tar)
    
    # 
    return

# A wrapper for Systematic Sim 2. Gets the localized placement
# as a normalized value, and distinguishes srcs from destinations.
# @param N = number of participents
# @param M = number of targets
# @return (src,dst,tar)
def getLocalizedPlacementNorm(N,M):
    # Obtain the source, destination and target coordinates
    # These are normalizied. 
    nodes, tar = ss2.getLocalizedPlacement(N,M)
    src = []; dst = [];
    for i,xy in enumerate(nodes):
        if i % 2 == 0:
            src.append(xy)
        else:
            dst.append(xy)
    del nodes
    return (src,dst,tar)
    
## Extracts 2 xy lists from a list of xy values
## @return [[x],[y]]
def extractXY(data):
    x = [xy[0] for xy in data]
    y = [xy[1] for xy in data]
    return [x,y]

def rep(item,n):
    return [item for i in range(n)]

## Quickly plots xy data
## @param data = a numpy array of [x,y] coordinates
def plot(data):
    x,y = extractXY(data)
    plt.scatter(x,y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    return

## Plots the game
## @param src = source coordinates
## @param dst = destination coordinates
## @param tar = target coordinates
def plotGame(src,dst,tar):
    x_src,y_src = extractXY(src)
    x_dst,y_dst = extractXY(dst)
    x_tar,y_tar = extractXY(tar)
    x = []; x.extend(x_src); x.extend(x_dst); x.extend(x_tar)
    y = []; y.extend(y_src); y.extend(y_dst); y.extend(y_tar)
    c = []; 
    c.extend(rep(0,len(src))); 
    c.extend(rep(1,len(dst)));
    c.extend(rep(2,len(tar)));
    d = {
        'x' : x,
        'y' : y,
        'c' : c
    }
    plt.scatter('x','y',c='c',data=d)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    return


if __name__ == "__main__":
    main()
