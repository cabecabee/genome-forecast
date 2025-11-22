from functions.prob_mut import prob_mut
from functions.mutate import mutate
from functions.verify_mutations import verify_mutations
from functions.analyze_mutations import analyze_mutations
from dicts.domains import domains

# ☹️

def repeat_mutations(lmbda, seq, p_cumulative, substitution_probs, loop_amount=10000):

    accumulator_table = {
        domain: {"missense": 0,
                 "nonsense": 0,
                 "missense_conservative": 0,
                 "missense_non_conservative": 0
        }
        for domain in domains.keys()
    }

    for i in range(loop_amount):
        mut_seq, mutations = mutate(lmbda, seq, p_cumulative, substitution_probs)
        result = analyze_mutations(seq, mut_seq, mutations)
        current_domain = verify_mutations(result["mut_types"])
        for domain in domains.keys():
            if domain == "nls":
                accumulator_table[domain]["missense_conservative"] += current_domain[domain]["missense_conservative"]
                accumulator_table[domain]["missense_non_conservative"] += current_domain[domain]["missense_non_conservative"]
            else:
                accumulator_table[domain]["missense"] += current_domain[domain]["missense"]
            accumulator_table[domain]["nonsense"] += current_domain[domain]["nonsense"]
    
    return accumulator_table