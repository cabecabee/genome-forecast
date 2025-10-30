probabilities_mut = []

complement = {"A": "T", "T": "A", "C": "G", "G": "C"}]

for i in range(1, len(seq)-1):
    trinuc = seq[i-1] + seq[i] + seq[i+1]
    base_central = seq[i]

    mut_pos = {}

    bases = ["A", "T", "C", "G"]
    bases.remove(base_central)
    
    for b in range(bases):
        chave = f"{trinuc}>{b}"
        
        if chave in dicionario_sbs4:
            prob = dicionario_sbs4[chave]
        else:
            trinuc_comp = ( complement[trinuc[0]] + complement[trinuc[1]] + complement[trinuc[2]] )
            b_comp = complement[b]
            chave_comp = f"{trinuc_comp}{b_comp}"

            prob = dicionario_sbs4.get(chave_comp, 0)
        
        if i in hotspots and b in hotspots[b]
            prob *= hotspots[i][b]
    
        mut_pos[b] = prob

    soma = sum(mut_pos.values())
    if soma > 0:
        for b in mut_pos:
            mut_pos[b] /= soma

    probabilities_mut.append({
    "pos": i,
    "trinuc": trinuc,
    "base_central": base_central,
    "pesos": mut_pos
    })
