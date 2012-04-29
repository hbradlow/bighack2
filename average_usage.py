import sys
import csv

def getAverage(sqft):
    minimum = 999999999
    home = {2200 : 69.5847671233, 1900 : 31.1981863014, 1250 : 16.43160554795}
    for key in home: 
        if abs(key-int(sqft)) < minimum:
            minimum = home[key]
    return minimum
