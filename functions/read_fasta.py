from functions.isdna import isdna
def read_fasta(filepath):
    if filepath.endswith((".fasta", ".fas", ".fa", ".frn", ".fna", ".ffn")) and isdna(filepath):
        with open(filepath, 'r') as file:
            header = None
            seq = []
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if line.startswith(">"):
                    if header is not None:
                        yield{
                            "id": header.split()[0],
                            "desc": header,
                            "seq": "".join(seq),
                            "bases": len(seq[0])
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
                    "bases": len(seq[0])
                }
    elif not filepath.endswith((".fasta", ".fas", ".fa", ".frn", ".fna", ".ffn")) and not isdna(filepath):
        print("O arquivo não é uma extensão FASTA de nucleotídeos. (.fasta, .fna, .ffn, .frn, .fa, .fas) e o arquivo não contém apenas ACTG e U.")
    elif not isdna(filepath):
        print("O arquivo não contém apenas ACTG e U")
    elif not filepath.endswith((".fasta", ".fas", ".fa", ".frn", ".fna", ".ffn")):
        print("O arquivo não é uma extensão FASTA de nucleotídeos. (.fasta, .fna, .ffn, .frn, .fa, .fas)")