""" BioE231
    Vivian Fu, Jessica Wu, Zihui Xu

    Create box plot that shows distribution of sequence lengths within each cluster.
    Input: unaligned FASTA sequences
    """

from Bio import SeqIO
import matplotlib.pylab as plt
import sys

ids = [('hu.43','hu.48','hu.44','hu.46','hu.14','hu.31','hu.32','rh.43'),('rh.61','rh.58','rh.53','rh.57','rh.51','rh.49','rh.53','rh.50','rh.52','hu.39'), ('hu.17','hu.6'), ('hu.41','rh.38','hu.42')]
num_clusters = len(ids)
# Find desired clusters' sequence lengths
seqs = {k: [] for k in range(0,num_clusters)}    # Initialize dictionary of clusters: sequences
for sequence in SeqIO.parse(sys.stdin, 'fasta'):
    for cluster in range(0,num_clusters):
        if sequence.id in ids[cluster]:
            seqs[cluster].append(len(sequence.seq))

for cluster, lens in seqs.items():
    print(cluster)
    print(lens)


#################### Input plot range
#plot_range = range(400, 600)
## Initialize dictionary of counts
#           # [A/T count, G/C count, indel count]
#content_dict = {k: [0,0,0] for k in plot_range}

#for seq in seqs:
#    for pos in plot_range:
#        if seq[pos] == 'A' or seq[pos] == 'T':
#            content_dict[pos][0] += 1
#        elif seq[pos] == 'C' or seq[pos] == 'G':
#            content_dict[pos][1] += 1
#        else:
#            content_dict[pos][2] += 1

## Normalize
#num_seqs = len(seqs)
#for pos, counts in content_dict.items():
#    content_dict[pos] = [count/num_seqs for count in counts]
    

## Plotting
#counts = sorted(content_dict.items())
#positions, counts = zip(*counts)
#
#AT_counts = [count[0] for count in counts]
#GC_counts = [count[1] for count in counts]
#ATGC_bottom = [count[0] + count[1] for count in counts]
#indel_counts = [count[2] for count in counts]
#
#plt.bar(positions, AT_counts, color = 'r')
#plt.bar(positions, GC_counts, bottom = AT_counts, color = 'b')
#plt.bar(positions, indel_counts, bottom = ATGC_bottom, color = 'y')

#plt.xlabel('Position in Sequence')
#plt.ylabel('%AT or %GC')
#plt.show()
