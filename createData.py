"""
Name: Dhaval Shrishrimal
file = createData.py
Description: this file creates a database with the given data file
"""

from PIL import Image
from globalVariables import *

def readImage(imageName, resultName, terrainArray):
    """
    Read the image file and create a terrain array
    Also, save a copy of the original file as result file
    """
    terrain = Image.open(imageName)
    result = terrain.copy()
    result.save(resultName)
    pixels = terrain.load()
    for x in range(MAX_LEN):
        for y in range(MAX_WID):
            terrainArray[x][y].append(pixels[y,x][:3])
    return terrainArray

def readElevation(elevationName, terrainArray):
    """
    this function reads the elevation filr and adds its values to
    the terrain array
    """
    elevationFile = open(elevationName)
    temp = list()
    for x in range(MAX_LEN):
        temp = elevationFile.readline().split("   ")
        temp.pop(0)
        for y in range(MAX_WID):
            terrainArray[x][y].append(float(temp[y]))
    elevationFile.close()
    return terrainArray
            

def createArray(imageName, resultName, elevationName):
    """
    this function initializes the terrainArray and calls the
    functions to populate the array
    """
    terrainArray = [[list() for i in range(MAX_WID)] \
        for j in range(MAX_LEN)]
    terrainArray = readImage(imageName, resultName, terrainArray)
    terrainArray = readElevation(elevationName, terrainArray)
    return terrainArray

