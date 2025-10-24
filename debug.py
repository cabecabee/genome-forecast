from functions.read_fasta import read_fasta
from functions.transcript import transcript
from functions.translate import translate
from functions.get_cds import get_cds
from functions.poisson import poisson
from functions.get_weights import get_weights

# dna = ""
# for i in read_fasta("fastafiles/p53.fasta"):
#     dna = dna.join(i["seq"])
# rna = transcript(dna)
# amino = translate(rna)
# print(amino)

from functions.mutate import mutate
from functions.duplicate import duplicate
duplicate("fastafiles/gene.fna", "duplicates/")
for i in read_fasta("duplicates/gene.fna"):
    dna = "".join(i["seq"])
cds = get_cds(dna)
print(len(cds))
#rna = transcript(dna)
#amino = translate(rna)
#print(amino)
# resultados como esperados!!! vamo gremio

