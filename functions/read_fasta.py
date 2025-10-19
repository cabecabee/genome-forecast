from functions.isdna import isdna

def read_fasta(filepath):
    valid_exts = (".fasta", ".fas", ".fa", ".frn", ".fna", ".ffn")

    if not filepath.endswith(valid_exts):
        print("O arquivo não é uma extensão FASTA de nucleotídeos. (.fasta, .fna, .ffn, .frn, .fa, .fas)")
        return

    if not isdna(filepath):
        print("O arquivo não contém apenas ACTG e U.")
        return

    with open(filepath, 'r') as file:
        header = None
        seq = []
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    yield {
                        "id": header.split()[0],
                        "desc": header,
                        "seq": "".join(seq),
                        "bases": len("".join(seq))
                    }
                header = line[1:]
                seq = []
            else:
                seq.append(line)
        if header is not None:
            yield {
                "id": header.split()[0],
                "desc": header,
                "seq": "".join(seq),
                "bases": len("".join(seq))
            }