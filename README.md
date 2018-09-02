## BioE231 Lab Assignment #2
Lab Partners: Vivian Fu, Jessica Wu, Zihui Xu

### Getting a phylogenetic tree
muscle -in seqs.fa -out seqs.aligned.fa  
Input: seqs.fa = unaligned protein and DNA/RNA sequences in FASTA format  
Output: seqs.aligned.fa = aligned sequences, as evident by dashes '-' that indicate indels

fasttree -nt < seqs.aligned.fa > tree.nwk

#### Visualize tree using Bio.Phylo  
python3 visualize_tree.py < tree.nwk

Obvious clusters of sequences are those that branch most recently (rightmost). In this case, 

#### Get sequences of a few IDs to BLAST  
python3 get_seqs.py < seqs.fa

### Identifying sequences by BLAST
