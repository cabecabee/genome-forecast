from functions.read_fasta import read_fasta
from functions.transcript import transcript
from functions.translate import translate

# dna = ""
# for i in read_fasta("fastafiles/p53.fasta"):
#     dna = dna.join(i["seq"])
# rna = transcript(dna)
# amino = translate(rna)
# print(amino)

from functions.mutate import mutate
from functions.duplicate import duplicate
duplicate("fastafiles/p53.fasta", "duplicates/")
mutate(0.5, "fastafiles/p53.fasta")

for i in read_fasta("duplicates/p53.fasta"):
    dna = "".join(i["seq"])
rna = transcript(dna)
amino = translate(rna)
print(amino)
# resultados como esperados!!! vamo gremio