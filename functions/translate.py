codigo_genetico = {
    # Fenilalanina
    "UUU": "Phe", "UUC": "Phe",
    # Leucina
    "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    # Isoleucina
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
    # Metionina (início)
    "AUG": "Met",
    # Valina
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    # Serina
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "AGU": "Ser", "AGC": "Ser",
    # Prolina
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    # Treonina
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    # Alanina
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    # Tirosina
    "UAU": "Tyr", "UAC": "Tyr",
    # Histidina
    "CAU": "His", "CAC": "His",
    # Glutamina
    "CAA": "Gln", "CAG": "Gln",
    # Asparagina
    "AAU": "Asn", "AAC": "Asn",
    # Lisina
    "AAA": "Lys", "AAG": "Lys",
    # Ácido aspártico
    "GAU": "Asp", "GAC": "Asp",
    # Ácido glutâmico
    "GAA": "Glu", "GAG": "Glu",
    # Cisteína
    "UGU": "Cys", "UGC": "Cys",
    # Triptofano
    "UGG": "Trp",
    # Arginina
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGA": "Arg", "AGG": "Arg",
    # Glicina
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    # Códons de parada
    "UAA": "Stop", "UAG": "Stop", "UGA": "Stop"
}


def translate(rna):
    proteina = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon in codigo_genetico:
            amino_acido = codigo_genetico[codon]
            if amino_acido == "Stop":
                break
            proteina.append(amino_acido)
    return ' '.join(proteina)
  
    