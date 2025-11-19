import time

from functions.user_data import user_data
from functions.read_fasta import read_fasta
from functions.prob_mut import prob_mut
from functions.repeat_mutations import repeat_mutations

lmbda, prevdec = user_data()

start = time.time()

seq = ""
for i in read_fasta("fastafiles/p53.fasta"):
    seq += i["seq"]
p_cumulative, probabilities_mut = prob_mut(seq)

domaintable = repeat_mutations(lmbda, seq, p_cumulative, probabilities_mut, 10000)

soma = sum(
    count
    for domain in domaintable.values()
    for count in domain.values()
)

percent = {
    domain: {mut_type: (count / soma) * 100 for mut_type, count in subdict.items()}
    for domain, subdict in domaintable.items()
}

print(percent)

end = time.time()

print(f"Tempo de execução: {end - start:.2f} segundos")