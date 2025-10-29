probabilities_mut = []

for i in range(1, len(seq)-1):
    trinuc = seq[i-1] + seq[i] + seq[i+1]
    base_central = seq[i]

    mut_pos = {}

    bases = ["A", "T", "C", "G"]
    bases.remove(base_central)
    
    for b in range(bases):
        chave = f"{trinuc}>{b}"
        prob = dicionario_sbs4.get(chave, 0)
        
        if i in hotspots and chave.split(">")[1] in hotspots[i]:
            prob *= hotspots[i][chave.split(">")[1]]
    
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
