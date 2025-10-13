def isdna(filepath):
    allowedchars = {"A", "C", "T", "G", "U"}
    sequence = ""
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            sequence += line
    sequence.upper()
    return all(base in allowedchars for base in sequence)
