from functions.read_fasta import read_fasta
from functions.prob_mut import prob_mut
seq = ""
for i in read_fasta("fastafiles/gene.fna"):
    seq = seq + i["seq"]
print(prob_mut(seq))