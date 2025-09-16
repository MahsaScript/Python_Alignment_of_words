# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 03:12:07 2021

@author: mahsa
"""

# Step 1: pip install bio -> anaconda prompt  I found at: https://pypi.org/project/bio/
# Step 2: Different alignment between two strings

from Bio import pairwise2
from Bio.Seq import Seq 
from Bio.pairwise2 import format_alignment 
sequence_string_1 = Seq("MNOPQ")  # m = 5 is the length of first string
sequence_string_2 = Seq("VWXYZ")  # n = 5 is the length of second string 


alignments_of_words = pairwise2.align.globalxx(sequence_string_1, sequence_string_2) # Get all of alignment

count=0 # counter for counting
for each_alignment in alignments_of_words: 
    count+=1
    print(format_alignment(*each_alignment)) # Illustrate alignments_of_words 
    
    print(each_alignment)

print('Count: %s' %(count)) # Print Total Count
