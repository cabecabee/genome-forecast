import random
def mutate_sequence(seq, mutationrate):
    """Aplica mutações aleatórias de acordo com a taxa fornecida (0–1)."""
    bases = ["A", "C", "T", "G"]
    seq_list = list(seq)

    for i in range(len(seq_list)):
        if random.random() < mutationrate:
            original = seq_list[i]
            seq_list[i] = random.choice([b for b in bases if b != original])

    return "".join(seq_list)