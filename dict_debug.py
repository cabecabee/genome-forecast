dicionario_sbs4 = {
    "ACA>A": 0.0421,
    "ACC>A": 0.0332,
    "ACG>A": 0.0155,
    "ACT>A": 0.0294,
    
    "ACA>G": 0.0068,
    "ACC>G": 0.0028,
    "ACG>G": 0.0012,
    "ACT>G": 0.0035,

    "ACA>T": 0.0086,
    "ACC>T": 0.0041,
    "ACG>T": 0.0007,
    "ACT>T": 0.0042,

    "ATA>A": 0.0094,
    "ATC>A": 0.0332,
    "ATG>A": 0.0155,
    "ATT>A": 0.0294
    
}

hotspots = {
    512: {"G>T": 3.0}
}

probabilities_mut = []

from functions.read_fasta import read_fasta
seq = ""
for i in read_fasta("duplicates/gene.fna"):
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
