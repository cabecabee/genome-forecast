def translate(rna):
    codon_table = {
        "UUU": "Phe", "UUC": "Phe",
        "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "AGU": "Ser", "AGC": "Ser",
        "UAU": "Tyr", "UAC": "Tyr",
        "UAA": "stop", "UAG": "stop", "UGA": "stop",
        "UGU": "Cys", "UGC": "Cys",
        "UGG": "Trp",
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        "CAU": "His", "CAC": "His",
        "CAA": "Gln", "CAG": "Gln",
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGA": "Arg", "AGG": "Arg",
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
        "AUG": "Met",
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        "AAU": "Asn", "AAC": "Asn",
        "AAA": "Lys", "AAG": "Lys",
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        "GAU": "Asp", "GAC": "Asp",
        "GAA": "Glu", "GAG": "Glu",
        "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
    }

    proteins = []
    i = 0
    while i < len(rna) - 2:
        codon = rna[i:i+3]
        if codon == "AUG":
            protein = []
            j = i
            while j < len(rna) - 2:
                current_codon = rna[j:j+3]
                amino = codon_table.get(current_codon, None)
                if amino == "stop":
                    break
                elif amino:
                    protein.append(amino)
                j += 3
            if protein:
                proteins.append(protein)
            i = j + 3
        else:
            i += 1
    return proteins