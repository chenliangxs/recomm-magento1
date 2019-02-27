# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 21:28:51 2019

@author: Silk
"""

from data import Data
from update import Update
'''
up = Update()
up.pickOrderRange('2018-10-01', '2019-01-01')
'''

data = Data()
trainY, trainR = data.getOrderData()
trainX = data.getFeatureData()
viewed = data.getViewedData()

print("TrainY: sizeX {}, sizeY {}".format(len(trainY), len(trainY[0])))
print("TrainR: sizeX {}, sizeY {}".format(len(trainR), len(trainR[0])))
print("TrainX: sizeX {}, sizeY {}".format(len(trainX), len(trainX[0])))
print("Viewed: sizeX {}, sizeY {}".format(len(viewed), len(viewed[0])))

'''
with open('trainY.txt', 'w') as file:
    for i in range(len(trainY)):
        for j in range(len(trainY[i])):
            file.write("%s\t" % trainY[i][j])
        file.write("\n")
        
with open('trainR.txt', 'w') as file:
    for i in range(len(trainR)):
        for j in range(len(trainR[i])):
            file.write("%s\t" % trainR[i][j])
        file.write("\n")
        
with open('trainX.txt', 'w') as file:
    for i in range(len(trainX)):
        for j in range(len(trainX[i])):
            file.write("%s\t" % trainX[i][j])
        file.write("\n")
        
with open('viewed.txt', 'w') as file:
    for i in range(len(viewed)):
        for j in range(len(viewed[i])):
            file.write("%s\t" % viewed[i][j])
        file.write("\n")
'''
with open('trainY.txt', 'w') as file:
    for i in range(100):
        for j in range(10):
            file.write("%s\t" % trainY[i][j])
        file.write("\n")
        
with open('trainR.txt', 'w') as file:
    for i in range(100):
        for j in range(10):
            file.write("%s\t" % trainR[i][j])
        file.write("\n")
        
with open('trainX.txt', 'w') as file:
    for i in range(100):
        for j in range(10):
            file.write("%s\t" % trainX[i][j])
        file.write("\n")

with open('viewed.txt', 'w') as file:
    for i in range(100):
        for j in range(10):
            file.write("%s\t" % viewed[i][j])
        file.write("\n")




