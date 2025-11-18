from functions.transcript import transcript
from functions.translate_linear import translate_linear

def analyze_mutations(orig_seq, mut_seq, mutations):
    # Transcrição e tradução
    orig_rna = transcript(orig_seq)
    mut_rna = transcript(mut_seq)
    orig_amino = translate_linear(orig_rna)
    mut_amino = translate_linear(mut_rna)

    # Achatando as listas de proteínas em uma só sequência linear de aminoácidos
    orig_amino = [aa for protein in orig_amino for aa in protein]
    mut_amino = [aa for protein in mut_amino for aa in protein]

    diffs = []
    mut_types = []

    for i, (a, b) in enumerate(zip(orig_amino, mut_amino)):
        if a != b:
            # Determina o tipo individual da mutação
            if b == "stop":
                mut_type = "nonsense"
            else:
                mut_type = "missense"
            diffs.append((i, a, b))
            mut_types.append((i, mut_type))

    changes = {
        "mut_amount": len(mutations),
        "mutations": mutations,
        "amino_diffs": diffs,           
        "mut_types": mut_types
    }

    return changes