def read_fasta(filepath):
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