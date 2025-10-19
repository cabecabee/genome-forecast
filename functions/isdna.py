def isdna(filepath):
    allowedchars = {"A", "C", "T", "G", "U"}
    sequenceparts = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            sequenceparts.append(line)
    sequence = "".join(sequenceparts).upper()
    return all(base in allowedchars for base in sequence)
