# -*- coding: utf-8 -*-
"""
Functions for working with Community Hawkes Independent Pairs (CHIP) models.

@author: Kevin S. Xu
"""

import sys
from os.path import join
sys.path.insert(0, join('..', '..', 'CHIP-Network-Model'))
import numpy as np
from dataset_utils import get_node_map

def load_facebook_chip(data_file_name, timestamp_max=1000):
    # sender_id receiver_id sender_id
    data = np.loadtxt(data_file_name, np.float)

    # Sorting by unix_timestamp and adjusting first timestamp to start from 0
    data = data[data[:, 2].argsort()]
    data[:, 2] = data[:, 2] - data[0, 2]

    if timestamp_max is not None:
        # Scale timestamps to 0 to timestamp_max
        data[:, 2] = (data[:, 2] - min(data[:, 2])) / (max(data[:, 2]) 
            - min(data[:, 2])) * timestamp_max

    duration = data[-1, 2]

    node_set = set(data[:, 0].astype(np.int)).union(data[:, 1].astype(np.int))
    node_id_map = get_node_map(node_set)

    event_dict = {}
    for i in range(data.shape[0]):
        receiver_id = node_id_map[np.int(data[i, 0])]
        sender_id = node_id_map[np.int(data[i, 1])]

        if (sender_id, receiver_id) not in event_dict:
            event_dict[(sender_id, receiver_id)] = []

        event_dict[(sender_id, receiver_id)].append(data[i, 2])

    return event_dict, len(node_set), duration
