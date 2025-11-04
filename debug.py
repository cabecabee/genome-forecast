from functions.prob_mut import prob_mut
from functions.read_fasta import read_fasta
from functions.user_data import user_data
from functions.mat_mut import mat_mut
lmbda = user_data()
seq = []
for i in read_fasta("fastafiles/p53.fasta"):
    seq.append(i["seq"])
seq = "".join(seq)
p_cumulative, probabilities_mut = prob_mut(seq)
print(mat_mut(lmbda, p_cumulative, probabilities_mut))