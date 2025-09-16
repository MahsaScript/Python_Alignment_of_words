# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 03:12:07 2021

@author: 
"""

# Step 1: pip install bio -> anaconda prompt  I found at: https://pypi.org/project/bio/
# Step 2: Different alignment between two strings: I found at: https://biopython.org/docs/1.75/api/Bio.pairwise2.html

from Bio import pairwise2
from Bio.Seq import Seq 
from Bio.pairwise2 import format_alignment 
sequence_string_1 = Seq("ABCDE")  # m = 5 is the length of first string
sequence_string_2 = Seq("RGHUJ")  # n = 5 is the length of second string 


alignments = pairwise2.align.globalxx(sequence_string_1, sequence_string_2) # Get all of alignment

count=0 # counter for counting
for alignment in alignments: 
    count+=1
    print(format_alignment(*alignment)) # Illustrate alignment 
    
    print(alignment)

print('Count: %s' %(count)) # Print Total Count
