def get_cds(seq):
    cds = ""
    seq = seq.upper()
    stop_codons = ["TAA", "TAG", "TGA"]
    i = 0
    while i < len(seq) - 3:
        codon = seq[i:i+3]
        if codon == "ATG":
            start = i
            for j in range(start, len(seq), 3):
                stop_codon = seq[j:j+3]
                if stop_codon in stop_codons:
                    cds += seq[start:j]
                    i = j + 3
                    break
            else:
                cds += seq[start:]
                break
        i += 1
    return cds