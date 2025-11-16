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

            if i in range(len(seq)):
                # checar todos os hotspots
                for pos_hot, muts in hotspots.items():
                    # pegar o códon do hotspot
                    codon_index = (pos_hot // 3) * 3
                    codon = seq[codon_index : codon_index+3]

                    # posição da base a mutar dentro do códon
                    pos_in_codon = pos_hot - codon_index

                    # checar se a posição do loop i está dentro do codon do hotspot
                    if i in range(codon_index, codon_index+3):
                        base_at_i = seq[i]

                        for key, mult in muts.items():
                            ref, mut = key.split(">")

                            # só aplica se a base do hotspot bate com a base real
                            if codon[pos_in_codon] == ref:
                                # calcular qual base do codon corresponde à posição i no trinuc
                                # posição relativa dentro do trinuc centrado em i
                                trinuc_start = i-1
                                pos_in_trinuc = pos_in_codon - (i - trinuc_start)
                                
                                # só aplica se a posição do hotspot cair na base central do trinuc
                                if pos_in_trinuc == 1:  
                                    if mut in mut_pos:
                                        mut_pos[mut] *= mult

        soma = sum(mut_pos.values())
        weights_position.append(soma)
        if soma > 0:
            for b in mut_pos:
                mut_pos[b] /= soma

        print(i, seq[i], seq[i-1:i+2])

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
