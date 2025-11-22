DOMAIN_WEIGHTS = {
    "tad": 2,
    "prd": 3,
    "dbd": 8,
    "nls_conservative": 1,
    "nls_non_conservative": 4,
    "od": 6,
    "ctd": 2
}

def normalize(accumulator, lambda_value):

    # 1 — soma total das categorias
    total = 0
    for d in accumulator.values():
        total += d.get("missense", 0)
        total += d.get("nonsense", 0)
        total += d.get("missense_conservative", 0)
        total += d.get("missense_non_conservative", 0)

    if total == 0:
        # sem mutações nos loops — retorna tudo zero
        return {
            dom: {
                "missense": 0,
                "nonsense": 0,
                "missense_conservative": 0,
                "missense_non_conservative": 0
            } for dom in accumulator
        }

    # 2 — converte accumulator → expected_counts baseados em λ
    expected = {}

    for dom, d in accumulator.items():

        expected[dom] = {}

        for key in ["missense", "nonsense",
                    "missense_conservative",
                    "missense_non_conservative"]:

            frac = d.get(key, 0) / total
            expected[dom][key] = frac * lambda_value   # <-- soma = λ

    return expected

def calculate_risk(counts):

    total_score = 0

    for domain, data in counts.items():

        # converte valores esperados → valores reais aproximados
        missense = data["missense"]
        nonsense = data["nonsense"]
        mc = data["missense_conservative"]
        mnc = data["missense_non_conservative"]

        # nonsense
        total_score += nonsense * 10

        if domain == "nls":
            total_score += mc * DOMAIN_WEIGHTS["nls_conservative"]
            total_score += mnc * DOMAIN_WEIGHTS["nls_non_conservative"]
        else:
            total_score += missense * DOMAIN_WEIGHTS[domain]

    return min(total_score, 10)