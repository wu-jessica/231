""" BioE231
    Vivian Fu, Jessica Wu, Zihui Xu

    Get sequences corresponding to given IDs.
    """

from Bio import SeqIO
import sys

ids = ['rh.40', 'hu.42', 'rh.13', 'rh.64']
for sequence in SeqIO.parse(sys.stdin, 'fasta'):
    if sequence.id in ids:
        print(sequence.id)
        print(sequence.seq + '\n')
