""" BioE231
    Vivian Fu, Jessica Wu, Zihui Xu

    Create bar plot of MSA within clusters.
    Input: aligned FASTA sequences
    """

from Bio import SeqIO
import matplotlib.pylab as plt
import sys


# Find desired sequences in cluster
ids = ['rh.58','rh.36', 'rh.37']
seqs = []
for sequence in SeqIO.parse(sys.stdin, 'fasta'):
    if sequence.id in ids:
        seqs.append(sequence.seq.upper())


#################### Input plot range
plot_range = range(400, 600)
# Initialize dictionary of counts
           # [A/T count, G/C count, indel count]
content_dict = {k: [0,0,0] for k in plot_range}

for seq in seqs:
    for pos in plot_range:
        if seq[pos] == 'A' or seq[pos] == 'T':
            content_dict[pos][0] += 1
        elif seq[pos] == 'C' or seq[pos] == 'G':
            content_dict[pos][1] += 1
        else:
            content_dict[pos][2] += 1

# Normalize
num_seqs = len(seqs)
for pos, counts in content_dict.items():
    content_dict[pos] = [count/num_seqs for count in counts]
    

# Plotting
counts = sorted(content_dict.items())
positions, counts = zip(*counts)

AT_counts = [count[0] for count in counts]
GC_counts = [count[1] for count in counts]
ATGC_bottom = [count[0] + count[1] for count in counts]
indel_counts = [count[2] for count in counts]

pAT = plt.bar(positions, AT_counts, color = 'r')
pCG = plt.bar(positions, GC_counts, bottom = AT_counts, color = 'b')
pND = plt.bar(positions, indel_counts, bottom = ATGC_bottom, color = 'y')

plt.xlabel('Position in Sequence')
plt.ylabel('%AT or %GC')
plt.legend([pAT,pCG,pND], ['AT','CG','indel'], bbox_to_anchor=(0,0,1.1,0.6))
plt.show()
