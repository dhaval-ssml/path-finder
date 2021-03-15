"""
Name: Dhaval Shrishrimal
File: main.py
Description: This file calls all the other files to create the terrainArray,
does the A8 search and displays the result.
"""

import sys

from globalVariables import *
from seasons import *
from createData import *
from aStar import *

def main():
    """
    This is the main entry point of the program
    """
    if len(sys.argv) != 6:
        print("Argument List: lab1.py terrainFile " \
            "elevationFile pathFile season outputFile")
        return
    else:  
        tArr = createArray(sys.argv[1], sys.argv[5], sys.argv[2])
        applySeason(sys.argv[4], tArr)
        path = open(sys.argv[3])
        first = path.readline().strip().split(" ")
        x = int(first[0])
        y = int(first[1])
        temp = list()
        total = 0
        for line in path:
            temp = line.split(" ")
            dist = traceBack(search(y, x, int(temp[1]), int(temp[0]), tArr)\
                , y, x, int(temp[1]), int(temp[0]), tArr, sys.argv[5])
            total += dist
            print("From area block (" + str(x) + ", " + str(y) + ") and (" \
                + temp[0] + ", " + temp[1].strip() + ") is " + str(dist) + " m.")
            x = int(temp[0])
            y = int(temp[1])
        print("Total distance travelled is " + str(total))
        return

if __name__ == "__main__":
    main()
            
