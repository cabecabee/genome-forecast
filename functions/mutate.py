import read_fasta
from genome_forecast import taxamutacao

def mutate(taxamutacao, fastafile): # Adquira essas informações por meio de input
    for i in read_fasta(fastafile):
        