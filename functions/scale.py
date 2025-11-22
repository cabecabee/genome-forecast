DOMAIN_WEIGHTS = {
    "tad": 2,
    "prd": 3,
    "dbd": 8,
    "nls_conservative": 1,
    "nls_non_conservative": 4,
    "od": 6,
    "ctd": 2
}

def mutation_weight(domain, mut_type, conservative=None): # obter o peso de uma mutação
    # nonsense dá o peso maximo
    if mut_type == "nonsense":
        return 10

    # missense depende do dominio
    if mut_type == "missense":

        # caso for nls, checa se é conservativa ou não
        if domain == "nls":
            if conservative:
                return DOMAIN_WEIGHTS["nls_conservative"]
            else:
                return DOMAIN_WEIGHTS["nls_non_conservative"]

        # para os outros dominios, faz o procedimento padrão
        return DOMAIN_WEIGHTS[domain]

    return 0 # fallback

def calculate_risk(counts): # risco total, recebe counts de verify_mutations
    total_score = 0

    for domain, data in counts.items():

        # nonsense
        total_score += data["nonsense"] * 10

        # missense, se for nls tem dois casos separados
        if domain == "nls":
            total_score += data["missense_conservative"] * DOMAIN_WEIGHTS["nls_conservative"]
            total_score += data["missense_non_conservative"] * DOMAIN_WEIGHTS["nls_non_conservative"]
        else:
            # missense comum
            total_score += data["missense"] * DOMAIN_WEIGHTS[domain]

    # normaliza para 1-10
    if total_score > 10:
        total_score = 10

    return total_score