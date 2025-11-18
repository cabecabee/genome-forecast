import time

from functions.user_data import user_data
from functions.read_fasta import read_fasta
from functions.prob_mut import prob_mut
from functions.mutate import mutate
from functions.analyze_mutations import analyze_mutations
from functions.repeat_mutations import repeat_mutations

lmbda = user_data()

start = time.time()

seq = ""
for i in read_fasta("fastafiles/p53.fasta"):
    seq += i["seq"]
p_cumulative, probabilities_mut = prob_mut(seq)

print(repeat_mutations(lmbda, seq, p_cumulative, probabilities_mut))

end = time.time()

print(f"Tempo de execução: {end - start:.2f} segundos")