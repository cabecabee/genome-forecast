from functions.dict_sbs4 import dicionario_sbs4

hotspots = {
    512: {"G>T": 3.0}
}

probabilities_mut = []

from functions.read_fasta import read_fasta
seq = ""
for i in read_fasta("fastafiles/gene.fna"):
    seq = seq + i["seq"]

for i in range(1, len(seq)-1):
    trinuc = seq[i-1] + seq[i] + seq[i+1]
    base_central = seq[i]

    mut_pos = {}

    bases = ["A", "T", "C", "G"]
    bases.remove(base_central)
    
    for b in bases:
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
print(prob)
