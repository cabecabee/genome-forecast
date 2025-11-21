from dicts.domains import domains
from dicts.conservativity import conservativity
def verify_mutations(mutations):
    counts = {
        domain: {
            "missense": 0,
            "nonsense": 0,
            "missense_conservative": 0,
            "missense_non_conservative": 0
        }
        for domain in domains.keys()
    }

    for pos, mut_type, original_aa, mutated_aa in mutations:
        domain = get_domain(pos)
        if domain is not None:
            counts[domain][mut_type] += 1

            if domain == "nls" and mut_type == "missense": # se estar no dominio nls e for missense verifica se é conservativa
                if mutated_aa in conservativity[original_aa]["conservative"]:
                    counts[domain]["missense_conservative"] += 1
                else:
                    counts[domain]["missense_non_conservative"] += 1

    return counts

def get_domain(pos):
    for name, coords in domains.items():
        if coords["start"] <= pos + 1 <= coords["end"]:
            return name
    return None