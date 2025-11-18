from functions.transcript import transcript

def analyze_mutations(orig_seq, mut_seq, mutations):
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
    orig_rna = transcript(orig_seq)

    codon_changes = translate_mut(orig_rna, mutations, codon_table)

    diffs = []
    mut_types = []

    for codon_index, orig_aa, mut_aa in codon_changes:
        if orig_aa != mut_aa:
            mut_type = "nonsense" if mut_aa == "stop" else "missense"
            diffs.append((codon_index, orig_aa, mut_aa))
            mut_types.append((codon_index, mut_type))

    return {
        "mut_amount": len(mutations),
        "mutations": mutations,
        "amino_diffs": diffs,
        "mut_types": mut_types
    }

def translate_mut(orig_seq, mutations, codon_table):
    results = []

    for nt_pos, orig_nt, new_nt in mutations:
        codon_index = nt_pos // 3
        start = codon_index * 3

        orig_codon = orig_seq[start:start+3]
        mut_codon_list = list(orig_codon)

        rna_nt = "U" if new_nt == "T" else new_nt

        mut_codon_list[nt_pos % 3] = rna_nt
        mut_codon = "".join(mut_codon_list)

        orig_aa = codon_table.get(orig_codon, None)
        mut_aa  = codon_table.get(mut_codon, None)

        results.append((codon_index, orig_aa, mut_aa))

    return results