#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Show a residue with different color

Tasks
=====
1. Obtain selected residues from interface as Python objects
2. Force display of such residues
3. Color those atoms in red
"""
import chimera

# 1
from chimera import runCommand as rc
rc("sel ligand zr < 5")
selected_residues = chimera.selection.currentResidues()

# 2
for residue in selected_residues:
    for atom in residue.atoms:
        atom.display = 1

# 3
from chimera.colorTable import getColorByName
red = getColorByName('red')
for residue in selected_residues:
    for atom in residue.atoms:
        atom.color = red
