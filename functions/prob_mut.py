from dicts.dict_sbs4 import dict_sbs4
from dicts.hotspots import hotspots

def prob_mut(seq):
    probabilities_mut = []
    weights_position = []

    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

    for i in range(1, len(seq)-1):
        trinuc = seq[i-1] + seq[i] + seq[i+1]
        base_central = seq[i]

        mut_pos = {}

        bases = ["A", "T", "C", "G"]
        if base_central in bases:
            bases.remove(base_central)
        
        for b in bases:
            chave = f"{trinuc}>{b}"
            
            if chave in dict_sbs4:
                prob = dict_sbs4[chave]
            else:
                trinuc_comp = complement[trinuc[0]] + complement[trinuc[1]] + complement[trinuc[2]]
                b_comp = complement[b]
                chave_comp = f"{trinuc_comp}>{b_comp}"

                prob = dict_sbs4.get(chave_comp, 0)
            
            mut_pos[b] = prob

        soma = sum(mut_pos.values())
        if i in hotspots:
            for key, mult in hotspots[i].items():
                ref, mut = key.split(">")
                # hotspot só vale se a base central for a ref
                if base_central == ref:
                    # aumenta o peso da mutação específica
                    if mut in mut_pos:
                        mut_pos[mut] *= mult
        soma = sum(mut_pos.values())
        weights_position.append(soma)
        if soma > 0:
            for b in mut_pos:
                mut_pos[b] /= soma

        probabilities_mut.append({
        "pos": i,
        "trinuc": trinuc,
        "base_central": base_central,
        "pesos": mut_pos
        })

    pp_tot = sum(weights_position)
    prob_pos = [p / pp_tot for p in weights_position]

    p_cumulative = []
    add = 0
    for p in prob_pos:
        add += p
        p_cumulative.append(add)

    return (p_cumulative, probabilities_mut)
