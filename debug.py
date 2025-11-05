import time

from functions.mat_mut import mat_mut
from functions.user_data import user_data
from functions.read_fasta import read_fasta
from functions.prob_mut import prob_mut

lmbda = user_data()

start = time.time()

seq = ""
for i in read_fasta("fastafiles/p53.fasta"):
    seq += i["seq"]
p_cumulative, probabilities_mut = prob_mut(seq)
outputlist = []
for i in range(100):
    outputlist.append(mat_mut(lmbda, p_cumulative, probabilities_mut))

end = time.time()

print(f"Tempo de execução: {end - start:.2f} segundos")