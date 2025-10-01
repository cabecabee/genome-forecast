def transcript(dna):

    transcricao = {
            'A': 'U',
            'T': 'A',
            'C': 'G',
            'G': 'C'
        }

    rna = ''.join([transcricao[base] for base in dna])
    return rna

#dna = "ATCGATCGATCG"
#print(transcript(dna))
