from functions.mat_mut import mat_mut

def mutate(lmbda, seq, p_cumulative, substitution_probs):
    seq = list(seq)
    mutations = mat_mut(lmbda, p_cumulative, substitution_probs)

    for pos, new_base in mutations:
        if 1 <= pos < len(seq):
            seq[pos - 1] = new_base
    
    return "".join(seq), mutations