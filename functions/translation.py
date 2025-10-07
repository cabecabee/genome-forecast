translate_table = {
    "Phe": {"UUU", "UUC"},
    "Leu": {"UUA", "UUG", "CUU", "CUC", "CUA", "CUG", "AGU", "AGC"},
    "Ser": {"UCU", "UCC", "UCA", "UCG"},
    "Tyr": {"UAU", "UAC"},
    "stop": {"UAA", "UAG", "UGA"},
    "Cys": {"UGU", "UGC"},
    "Trp": {"UGG"},
    "Pro": {"CCU", "CCC", "CCA", "CCG"},
    "His": {"CAU", "CAC"},
    "Gln": {"CAA", "CAG"},
    "Arg": {"CGU", "CGC", "CGA", "CGG", "AGA", "AGG"},
    "Ile": {"AUU", "AUC", "AUA"},
    "Met": {"AUG"},
    "Thr": {"ACU", "ACC", "ACG", "ACA"},
    "Asn": {"AAU", "AAC"},
    "Lys": {"AAA", "AAG"},
    "Val": {"GUU", "GUC", "GUA", "GUG"},
    "Ala": {"GCU", "GCC", "GCA", "GCG"},
    "Asp": {"GAU", "GAC"},
    "Glu": {"GAA", "GAG"},
    "Gly": {"GGU", "GGC", "GGA", "GGG"}
}

# isto ainda não é uma função!!!! quando estiver em casa eu transformo em uma :)

rna = "CGCAAUGGCGGA"
codons = []
if len(rna) % 3 != 0:
    print("Não é múltiplo de 3.")
else:
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)]

aminoacidos = []
for codon in codons:
    for amino, codonset in translate_table.items():
        if codon in codonset:
            aminoacidos.append(amino)
            break
print(aminoacidos)