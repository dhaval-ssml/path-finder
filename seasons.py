"""
Name: Dhaval Shrishrimal
File: seasons.py
Description: this file changes the terrainMap depending on the weather
"""

from globalVariables import *

SMR = "summer"
FAL = "fall"
WTR = "winter"
SPR = "spring"

def findNeighbors(x1, y1):
    """
    find the neighbors of pixel (x1, y1)
    """
    temp = list()
    if x1 == 0 and y1 == 0:
        temp.append((x1 + 1, y1 + 1))
        temp.append((x1, y1 + 1))
        temp.append((x1 + 1, y1))
    elif x1 == MAX_LEN - 1 and y1 == 0:
        temp.append((x1 - 1, y1 + 1))
        temp.append((x1, y1 + 1))
        temp.append((x1 - 1, y1))
    elif x1 == 0 and y1 == MAX_WID - 1:
        temp.append((x1 + 1, y1 - 1))
        temp.append((x1, y1 - 1))
        temp.append((x1 + 1, y1))
    elif x1 == MAX_LEN - 1 and y1 == MAX_WID - 1:
        temp.append((x1 - 1, y1 - 1))
        temp.append((x1, y1 - 1))
        temp.append((x1 - 1, y1))
    elif x1 == 0:
        temp.append((x1 + 1, y1 + 1))
        temp.append((x1 + 1, y1 - 1))
        temp.append((x1, y1 + 1))
        temp.append((x1, y1 - 1))
        temp.append((x1 + 1, y1))
    elif y1 == 0:
        temp.append((x1 + 1, y1 + 1))
        temp.append((x1 - 1, y1 + 1))
        temp.append((x1, y1 + 1))
        temp.append((x1 - 1, y1))
        temp.append((x1 + 1, y1))
    elif x1 == MAX_LEN - 1:
        temp.append((x1 - 1, y1 + 1))
        temp.append((x1 - 1, y1 - 1))
        temp.append((x1, y1 + 1))
        temp.append((x1, y1 - 1))
        temp.append((x1 - 1, y1))
    elif y1 == MAX_WID - 1:
        temp.append((x1 + 1, y1 - 1))
        temp.append((x1 - 1, y1 - 1))
        temp.append((x1, y1 - 1))
        temp.append((x1 - 1, y1))
        temp.append((x1 + 1, y1))
    else:
        temp.append((x1 + 1, y1 + 1))
        temp.append((x1 - 1, y1 + 1))
        temp.append((x1 + 1, y1 - 1))
        temp.append((x1 - 1, y1 - 1))
        temp.append((x1, y1 + 1))
        temp.append((x1, y1 - 1))
        temp.append((x1 + 1, y1))
        temp.append((x1 - 1, y1))
    return temp

def applySeason(season, tArr):
    """
    apply the season changes to the terrainMap
    """
    if season == SMR:
        return
    elif season == FAL:
        modifyFall(tArr)
    elif season == WTR:
        modifyWinter(tArr)
    elif season == SPR:
        modifySpring(tArr)

def modifyFall(tArr):
    """
    Modify the terrain Map if the weather outside is fall
    """
    temp = list()
    for x in range(MAX_LEN):
        for y in range(MAX_WID):
            if tArr[x][y][0] == FUT_PTH[0]:
                temp = findNeighbors(x, y)
                for neighbor in temp:
                    if tArr[neighbor[0]][neighbor[1]][0] == ESY_MOV[0]:
                        tArr[x][y][0] = LFY_PTH[0]
    return

def BFSWinter(tArr, ToVisit):
    """
    Does the BFS search converting all the water 7 pixels
    from water into ice
    """
    while not len(ToVisit) == 0:
        first = ToVisit.pop()
        depth = 0
        visitItr = list()
        visitItr.append(first)
        for i in visitItr:
            temp = findNeighbors(i[0], i[1])
            for neighbor in temp:
                if tArr[neighbor[0]][neighbor[1]][0] == WTR_BDY[0]:
                    tArr[neighbor[0]][neighbor[1]][0] = ICE_PTH[0]
                    if depth < 7:
                        visitItr.append(neighbor)
            depth += 1


def modifyWinter(tArr):
    """
    Modify the terrain if the weather is winter
    """
    ToVisit = set()
    for x in range(MAX_LEN):
        for y in range(MAX_WID):
            if tArr[x][y][0] == WTR_BDY[0]:
                temp = findNeighbors(x, y)
                for neighbor in temp:
                    if tArr[neighbor[0]][neighbor[1]][0] != WTR_BDY[0]:
                        ToVisit.add((x, y))
    BFSWinter(tArr, ToVisit)

def BFSSpring(tArr, ToVisit):
    """
    Does the BFS search converting all the water 7 pixels
    from land into mud
    """
    while not len(ToVisit) == 0:
        first = ToVisit.pop()
        depth = 0
        visitItr = list()
        visitItr.append(first)
        for i in visitItr:
            temp = findNeighbors(i[0], i[1])
            for neighbor in temp:
                if tArr[neighbor[0]][neighbor[1]][0] != WTR_BDY[0] and abs(tArr[neighbor[0]][neighbor[1]][1] - tArr[first[0]][first[1]][1]) < 1:
                    tArr[neighbor[0]][neighbor[1]][0] = MUD_PTH[0]
                    if depth < 15:
                        visitItr.append(neighbor)
            depth += 1

def modifySpring(tArr):
    """
    Modify the terrain if the weather is spring
    """
    ToVisit = set()
    for x in range(MAX_LEN):
        for y in range(MAX_WID):
            if tArr[x][y][0] != WTR_BDY[0]:
                temp = findNeighbors(x, y)
                for neighbor in temp:
                    if tArr[neighbor[0]][neighbor[1]][0] == WTR_BDY[0]:
                        ToVisit.add((x, y))
    BFSSpring(tArr, ToVisit)
