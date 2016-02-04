#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Bonus
=====
Save the selected sequence in an ordered list and convert
the three letter code to single letter code in a single string
"""
import chimera

all_opened_molecules = chimera.openModels.list()
protein = all_opened_molecules[0]

save_sequence = []
for residue in protein.residues:
    save_sequence.append(residue.type)
print save_sequence[0]

for aa in save_sequence:
    print chimera.resCode.res3to1(aa)