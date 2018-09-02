## BioE231 Lab Assignment #2
Lab Partners: Vivian Fu, Jessica Wu, Zihui Xu

### Getting a phylogenetic tree
muscle -in seqs.fa -out seqs.aligned.fa  
Input: seqs.fa = unaligned protein and DNA/RNA sequences in FASTA format  
Output: seqs.aligned.fa = aligned sequences, as evident by dashes '-' that indicate indels

fasttree -nt < seqs.aligned.fa > tree.nwk

#### Visualize tree using Bio.Phylo  
python3 visualize_tree.py < tree.nwk

Obvious clusters of sequences are those that branched most recently (more to the right). In this case,
rh.40, rh.38, hu.67, 37, 40, 66, 41, and 42 are an obvious cluster. Pairs or groups of sequences that
seem very closely related also branch more to the right, for instance hu.44 and hu.46. Sequences that
seem more distantly related than others are those that diverged earlier (more to the left). For this
tree, rh.13, rh.64, and hu.32 are distantly related to each other.

We chose to use BLAST to more closely examine the sequences of rh.40, hu.42, rh.13, rh.64, and hu.32,
which span clusters of both like and unlike sequences.

#### Get a few sequences to BLAST  
python3 get_seqs.py < seqs.fa

### Identifying sequences by BLAST
