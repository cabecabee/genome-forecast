from functions.read_fasta import read_fasta

def mutate(mutationrate, fastafile): # Adquira essas informações por meio de input
    for i in read_fasta(fastafile):
        mutations = i["bases"] / mutationrate
        print("Mutações: %d" % mutations)
