import time

from functions.user_data import user_data
from functions.read_fasta import read_fasta
from functions.prob_mut import prob_mut
from functions.mutate import mutate
from functions.analyze_mutations import analyze_mutations

lmbda = user_data()

start = time.time()

seq = ""
for i in read_fasta("fastafiles/p53.fasta"):
    seq += i["seq"]
p_cumulative, probabilities_mut = prob_mut(seq)

mut_seq, mutations = mutate(lmbda, seq, p_cumulative, probabilities_mut)
result = analyze_mutations(seq, mut_seq, mutations)

for i, original, mutado in result["amino_diffs"]:
    if mutado == "stop":
        tipo = "nonsense"
    elif original != mutado:
        tipo = "missense"
    else:
        tipo = "sinônima"
    print(f"Aminoácido {i}: {original} → {mutado} ({tipo})")

end = time.time()

print(f"Tempo de execução: {end - start:.2f} segundos")