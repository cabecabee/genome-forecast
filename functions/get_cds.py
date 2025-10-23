def get_cds(seq):
    start = seq.find("ATG")
    if start == -1:
        start = 0
    stop_codons = ["TAA", "TAG", "TGA"]
    for i in range(start, len(seq), 3):
        codon = seq[i:i+3]
        if codon in stop_codons:
            return seq[start:i]
    return seq[start:]