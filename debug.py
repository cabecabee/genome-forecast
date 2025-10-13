from functions.read_fasta import read_fasta
from functions.transcript import transcript
from functions.translate import translate
from functions.isdna import isdna

dna = ""
for i in read_fasta("fastafiles/p53.fasta"):
    dna = dna.join(i["seq"])
rna = transcript(dna)
amino = translate(rna)
print(amino)