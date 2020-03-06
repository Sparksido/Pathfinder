# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:10:04 2020

@author: 26772
"""
nodes = {"1":{"2":3,"6":5},"2":{"3":7,"6":10}}
nodesMatrix = [[0,  3,  1000,  1000,  1000,  5],
               [1000,  0,  7,  1000,  1000,  10],
               [1000,  1000,  0,  5,  1,  1000],
               [1000,  1000,  1000,  0,  6,  1000],
               [1000,  1000,  1000, 1000,  0,  7],
               [1000,  1000,  8,  2,  1000,  0]]

iteration = 1
visited = [1]
unvisitedSize = len(nodesMatrix)
unvisited = []
counter = 1

while counter < unvisitedSize:
    unvisited.append(counter + 1)
    counter = counter + 1


print(unvisited)

