# -*- coding: utf-8 -*-
"""
Python code of Feature Selection using Gravitational Search Algorithm (GSA) and Support Vector Machine (SVM)
Purpose: Defining the gConstant Function
            for calculating the Gravitational Constant

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy

def gConstant(l,iters):
    alfa = 20
    G0 = 100
    Gimd = numpy.exp(-alfa*float(l)/iters)
    G = G0*Gimd
    return G
