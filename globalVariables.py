"""
Name: Dhaval Shrishrimal
File: globalVariables.py
Description: This file carries all the global variable values of the program
"""
import math

tArr = None

# max values to loop over
MAX_WID = 395
MAX_LEN = 500

# terrain type values with their speeds
OPN_LND = [(248, 148, 18), 1]
RGH_MED = [(255, 192, 0), 1.5]
ESY_MOV = [(255, 255, 255), 1.2]
SLW_RUN = [(2, 208, 60), 1.3]
WLK_FOR = [(2, 136, 40), 1.4]
IMP_VEG = [(5, 73, 24), math.inf]
WTR_BDY = [(0, 0 ,255), math.inf]
PVD_RDS = [(71, 51, 3), 1]
FUT_PTH = [(0, 0 ,0), 1.1]
OUT_BND = [(205, 0, 101), math.inf]
LFY_PTH = [(160, 160, 160), 1.2]
ICE_PTH = [(102, 255, 255), 1.3]
MUD_PTH = [(102, 51, 0), 1.5]

# terrian type used for the marked path
PTH_RED = (255, 0 , 0)

# pixel to real life distance
xDist = 10.29
yDist = 7.55
