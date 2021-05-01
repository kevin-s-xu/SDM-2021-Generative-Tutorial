# -*- coding: utf-8 -*-
"""
Script to import adjacency matrices from Facebook data and filter out
low-degree nodes to leave a small network with only a few hundred nodes.

This script should be applied to Facebook friendship and wall post data
collected by Viswanath et al. (2009) to prepare it for the SDM 2021
tutorial demos.

Download data from link below and save it in the ../data folder.

Data source: http://socialnetworks.mpi-sws.org/data-wosn2009.html

@author: Kevin S. Xu
"""

wallCutoff = 50
startTime = 1167627600
endTime = 1199163600

from os.path import join
import numpy as np
import networkx as nx

#%% Import wall post network from edge list
# Create digraph from edge list in text file. The edge list is in format
#   recipient poster timestamp
# while NetworkX expects
#   fromNode toNode
# so we load the timestamp as an edge attribute (of type int) and then
# reverse the digraph so that the edges are in the proper direction.
print('Loading wall edge list')
dataFileName = join('..', 'data', 'facebook-wall.txt')
# fbWall = nx.read_edgelist(dataFileName,create_using=nx.MultiDiGraph(),
#                           data=(('Timestamp',int),)).reverse()
# print('Removing all self-edges')
# selfEdges = list(nx.selfloop_edges(fbWall))
# fbWall.remove_edges_from(selfEdges)

# receiver_id sender_id unix_timestamp
data = np.loadtxt(dataFileName, np.int32)
# Remove self-edges
data = data[np.where(data[:,0] != data[:,1])[0],:]
# Remove edges outside of start and end times
data = data[np.where(data[:,2] >= startTime)[0],:]
data = data[np.where(data[:,2] < endTime)[0],:]

fbWall = nx.MultiDiGraph()
for i in range(data.shape[0]):
    fbWall.add_edge(data[i,1],data[i,0],Timestamp=data[i,2])
print('%i nodes' % fbWall.number_of_nodes())
print('Removing all nodes with both in- and out-degree less than %i'
      % wallCutoff)
wallInDeg = dict(fbWall.in_degree)
wallOutDeg = dict(fbWall.out_degree)
for nodeId,inDeg in wallInDeg.items():
    outDeg = wallOutDeg[nodeId]
    if (inDeg < wallCutoff) and (outDeg < wallCutoff):
        fbWall.remove_node(nodeId)
print('%i nodes' % fbWall.number_of_nodes())
print('Removing all nodes that now have both in- and out-degree 0')
wallNodes = list(fbWall.nodes)
for nodeId in wallNodes:
    if (fbWall.in_degree[nodeId] == 0) and (fbWall.out_degree[nodeId] == 0):
        fbWall.remove_node(nodeId)
print('%i nodes' % fbWall.number_of_nodes())
print('Saving filtered wall post edge list')
outDataFileName = join('..', 'data', 'facebook-wall-filtered.txt')
nx.write_edgelist(fbWall,outDataFileName,data=['Timestamp'])

