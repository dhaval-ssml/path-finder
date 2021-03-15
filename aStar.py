"""
Name: Dhaval Shrishrimal
File: aStar.py
Description: this file is responsible for conducting an Astar search
between two pixels and update the result with an optimal path
"""

import math
from globalVariables import *
from queue import PriorityQueue
from PIL import Image
from seasons import *

def calcDistance(x1, y1, x2, y2, tArr):
    """
    calculate the distance between 2 points
    h(n) function
    """
    elev = abs(tArr[x1][y1][1] - tArr[x2][y2][1])
    x = abs(x1 - x2) * xDist
    y = abs(y1 - y2) * yDist
    return math.pow((math.pow(x, 2) + math.pow(y, 2) + math.pow(elev, 2)), 0.5)

def calcG(x1, y1, x2, y2, tArr):
    """
    calculate the cost of going from a node to another
    g(n) function
    """
    dist = calcDistance(x1, y1, x2, y2, tArr)
    if tArr[x2][y2][0] == OPN_LND[0] or tArr[x2][y2] == PVD_RDS[0]:
        return dist * OPN_LND[1]
    elif tArr[x2][y2][0] == FUT_PTH[0]:
        return dist * FUT_PTH[1]
    elif tArr[x2][y2][0] == ESY_MOV[0] or tArr[x2][y2][0] == LFY_PTH[0]:
        return dist * ESY_MOV[1] 
    elif tArr[x2][y2][0] == SLW_RUN[0] or tArr[x2][y2][0] == ICE_PTH[0]:
        return dist * SLW_RUN[1] 
    elif tArr[x2][y2][0] == WLK_FOR[0] or tArr[x2][y2][0] == MUD_PTH[0]:
        return dist * WLK_FOR[1]  
    elif tArr[x2][y2][0] == RGH_MED[0]:
        return dist * RGH_MED[1]
    else:
        return math.inf 

def calcCost(x1, y1, x2, y2, x3, y3, tArr):
    """
    calculates the total cost/heuristic for A* search
    f(n) function
    """
    cost = calcG(x1, y1, x2, y2, tArr) + calcDistance(x2, y2, x3, y3, tArr)
    return cost

def search(xStart, yStart, xDest, yDest, tArr):
    """
    the A* implementation, find the path from source 
    to destination
    """
    parentNeighbor = dict()
    closed = set()
    openS = set()
    openQ = PriorityQueue()
    openQ.put((1, (xStart, yStart)))
    openS.add((xStart, yStart))
    while not openQ.empty():
        pixQ = openQ.get()
        pix = pixQ[1]
        openS.remove(pix)
        closed.add(pix)
        neighbors = findNeighbors(pix[0], pix[1])
        for neighbor in neighbors:
            if xDest == neighbor[0] and yDest == neighbor[1]:
                parentNeighbor[neighbor] = pix
                return parentNeighbor
            if not (neighbor in openS or neighbor in closed):
                openS.add(neighbor)
                priority = calcCost(pix[0], pix[1], \
                    neighbor[0], neighbor[1], xDest, yDest, tArr)
                openQ.put((priority, neighbor))
                parentNeighbor[neighbor] = pix
    return False

def traceBack(parentNeighbor, xStart, yStart, xDest, yDest, tArr, resultName):
    """
    this file traceback and updates the final map once A* has finished 
    finding the optimal path
    """
    x = xDest
    y = yDest
    totalDistance = 0
    final = Image.open(resultName)
    pixels = final.load()
    for xID in range(MAX_LEN):
        for yID in range(MAX_WID):
            pixels[yID, xID] = tArr[xID][yID][0]
    while True:
        if x == xStart and y == yStart:
            tArr[x][y][0] = PTH_RED
            pixels[y, x] = PTH_RED
            final.save(resultName)
            totalDistance += calcDistance(x, y, xStart, yStart, tArr)
            return totalDistance
        else:
            tArr[x][y][0] = PTH_RED
            pixels[y, x] = PTH_RED
            xNew, yNew = parentNeighbor.get((x, y))
            totalDistance += calcDistance(x, y, xNew, yNew, tArr)
            x, y = xNew, yNew
    return totalDistance
