#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Print the list of serial numbers of selected atoms... if they are not hydrogen!

Tasks
=====
1. Get current selection of atoms
2. Print serial numbers of all atoms
3. Print only those that are carbons
4. Save only those that are not hydrogens
5. Count polar residues in opened protein
6. Save and count at the same time?
"""

import chimera

# 1
selected_atoms = chimera.selection.currentAtoms()

# 2
for atom in selected_atoms:
    print atom.serialNumber

# 3 
for atom in selected_atoms:
    if atom.element.name == 'C':
        print atom.serialNumber

# 4
not_hydrogens = []
for atom in selected_atoms:
    if atom.element.name != 'H': # alternatively: if not atom.element.name == H:
        not_hydrogens.append(atom)

# 5
protein = chimera.selection.currentMolecules()[0]
polar_residues = ["GLN", "ASN", "HIS", "SER", "THR", "TYR", "CYS", "MET", "TRP"]

i = 0 # number of polar residues
for residue in protein.residues:
    if residue.type in polar_residues:
        i = i + 1 # same as i += 1

# 6
saved_polar_residues = []
for residue in protein.residues:
    if residue.type in polar_residues:
        saved_polar_residues.append(residue)
i = len(saved_polar_residues)