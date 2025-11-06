from functions.transcript import transcript
from functions.translate import translate

def analyze_mutations(orig_seq, mut_seq, mutations):
    orig_rna = transcript(orig_seq)
    mut_rna = transcript(mut_seq)
    orig_amino = translate(orig_rna)
    mut_amino = translate(mut_rna)

    # achatando as listas de proteínas em uma só sequência linear de aminoácidos
    orig_amino = [aa for protein in orig_amino for aa in protein]
    mut_amino = [aa for protein in mut_amino for aa in protein]

    diffs = []
    for i, (a, b) in enumerate(zip(orig_amino, mut_amino)):
        if a != b:
            diffs.append((i, a, b))
    
    if not diffs:
        type_mut = "sinônima"
    else:
        mut_bases = [b for (_, _, b) in diffs]
        if "stop" in mut_bases:
            type_mut = "nonsense"
        else:
            type_mut = "missense"

    changes = {
        "mut_amount": len(mutations),
        "mutations": mutations,
        "amino_diffs": diffs,
        "type": type_mut
    }

    return changes