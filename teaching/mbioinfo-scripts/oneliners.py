#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Oneliners

Useful commands in a single line!
"""

import chimera

# Serial number of current atom
chimera.selection.currentAtoms()[0].serialNumber

# Number of selected atoms
len(chimera.selection.currentAtoms())

# Total mass of selected protein
sum([a.element.mass for a in chimera.selection.currentMolecules()[0].atoms])

# Sequence of the whole protein
''.join([chimera.resCode.res3to1(aa.type) for aa in chimera.selection.currentMolecules()[0].residues])