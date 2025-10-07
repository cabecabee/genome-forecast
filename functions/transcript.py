def transcript(dna):

    transcricao = {
            'A': 'A',
            'T': 'U',
            'C': 'C',
            'G': 'G'
        }

    rna = ''.join([transcricao[base] for base in dna])
    return rna

#dna = "ATCGATCGATCG"
#print(transcript(dna))
