def transcript(dna):

    #transcricao = {
    #        'A': 'A',
    #        'T': 'U',
    #        'C': 'C',
    #        'G': 'G'
    #    }

    #rna = ''.join([transcricao[base] for base in dna])
    #return rna

    return dna.replace("T", "U")

#dna = "ATCGATCGATCG"
#print(transcript(dna))


# dna.replace("T", "U")