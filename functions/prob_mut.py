from dicts.dict_sbs4 import dict_sbs4
from dicts.hotspots import hotspots

def prob_mut(seq):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

    totals = []
    substitution_probs = []

    for i in range(1, len(seq)-1):
        original = seq[i]
        trinuc = seq[i-1] + seq[i] + seq[i+1]

        rates = {}

        for b in ["A", "T", "C", "G"]:
            if b == original: # para não mutar para a mesma base
                continue

            key = f"{trinuc}>{b}"

            if key in dict_sbs4:
                rate = dict_sbs4[key]
            else:
                trinuc_comp = (complement[trinuc[0]] +
                               complement[trinuc[1]] +
                               complement[trinuc[2]])

                b_comp = complement[b]
                key_comp = f"{trinuc_comp}>{b_comp}"

                rate = dict_sbs4.get(key_comp, 0)

            rates[b] = rate

        total_rate = sum(rates.values())

        if i in hotspots:
            for mut_key, fold in hotspots[i].items():

                old_base, new_base = mut_key.split(">")
                if original == old_base and new_base in rates:
                    rates[new_base] *= fold

            total_rate = sum(rates.values())

        totals.append(total_rate)

        if total_rate > 0:
            probs = {b: (rates[b] / total_rate) for b in rates}
        else:
            probs = {b: 0 for b in rates}

        substitution_probs.append({
            "pos": i,
            "original": original,
            "trinuc": trinuc,
            "rates": rates,
            "probs": probs
        })

    total_sum = sum(totals)

    if total_sum > 0:
        normalized = [t / total_sum for t in totals]
    else:
        normalized = [0] * len(totals)

    p_cumulative = []
    running = 0
    for n in normalized:
        running += n
        p_cumulative.append(running)

    return p_cumulative, substitution_probs