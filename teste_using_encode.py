#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:39:11 2021

@author: nicole
"""

import pandas as pd
import numerical_hash as nh

hashes_fd = pd.read_csv('hashes.csv')

encoding_hashes = nh.encodeHashList(hashes_fd, 'hash', 'dog')

encoding_hashes.to_csv('encoding_hashes.csv', index=False)

