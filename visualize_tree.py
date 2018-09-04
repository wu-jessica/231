""" BioE231
    Vivian Fu, Jessica Wu, Zihui Xu

    Use Biopython's Phylo to visualize tree.nwk. 
    """

from Bio import Phylo
from io import StringIO
import sys

tree = Phylo.read(sys.stdin, 'newick')
Phylo.draw(tree)
