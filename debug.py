from functions.user_data import user_data
from functions.read_fasta import read_fasta
from functions.prob_mut import prob_mut
from functions.mutate import mutate

lambida = user_data()

seq = next(read_fasta("fastafiles/p53.fasta"))["seq"]

p_cumulative, probabilities_mut = prob_mut(seq)

mutate(lambida, "fastafiles/p53.fasta", p_cumulative, probabilities_mut)