from functions.transcript import transcript
from functions.read_fasta import read_fasta
def translate(rna):
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
    metindex = -1
    for i in range(len(rna) - 2):
        codon = rna[i:i+3]
        if codon == "AUG":
            metindex = i
            break
    if metindex == -1:
        return []
    
    aminoacidos = []
    for i in range(metindex, len(rna)-2, 3):
        codon = rna[i:i+3]
        if codon in translate_table["stop"]:
            break
        for amino, codonset in translate_table.items():
            if codon in codonset:
                aminoacidos.append(amino)
                break
    return aminoacidos