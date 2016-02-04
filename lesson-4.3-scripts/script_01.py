#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Use Chimera Python API to print the sequence of aminoacids of an open protein

Prerequisites
=============
1. You should have an open protein already
2. If not, type "open PDBCODE" un command line, where PDBCODE is the 4 characters ID of a PDB entry

Tasks
=====
1. Retrieve opened protein as a Python object
2. Access its attributes and understand the underlying object architecture
3. Use a loop to iterate through all the residues in the protein and print its name
3.1. Print those in a single line, separated by dashes
"""
import chimera

# 1
all_opened_molecules = chimera.openModels.list()
protein = all_opened_molecules[0]

# 2
print protein.name
print protein.atoms

first_atom = protein.atoms[0]
print first_atom.name
print first_atom.element.name
print first_atom.name, first_atom.element.name

# 3
for residue in protein.residues:
    print residue.id.position, residue.type

for residue in protein.residues:
    print residue.type + "-",

