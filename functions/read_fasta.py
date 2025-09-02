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
                        "seq": "".join(seq)
                    }
                header = line[1:]
                seq = []
            else:
                seq.append(line)
        if header is not None:
            yield {
                "id": header.split()[0],
                "desc": header,
                "seq": "".join(seq)
            }

for i in read_fasta("fastafiles/homo.fasta"):
    print("ID:", i["id"])
    print("Descrição:", i["desc"])
    print("Sequência:", i["seq"])