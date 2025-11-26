from functions.repeat_mutations import repeat_mutations
from functions.mat_mut import mat_mut
def pelomenosum(lmbda, seq, p_cumulative, probabilities_mut, simulations=50000):
    E = 2.718281828459
    domaintable = repeat_mutations(lmbda, seq, p_cumulative, probabilities_mut, simulations)
    soma = sum(
        count
        for domain in domaintable.values()
        for count in domain.values()
    )

    percent = {
        domain: {mut_type: (count / soma) * 100 for mut_type, count in subdict.items()}
        for domain, subdict in domaintable.items()
    }

    media_dominio1missense = lmbda * percent['tad']['missense'] / 100
    media_dominio1nonsense = lmbda * percent['tad']['nonsense'] / 100

    media_final_dominio1missense = 1 - E**(-media_dominio1missense)
    media_final_dominio1nonsense = 1 - E**(-media_dominio1nonsense)

    media_dominio2missense = lmbda * percent['prd']['missense'] / 100
    media_dominio2nonsense = lmbda * percent['prd']['nonsense'] / 100
    
    media_final_dominio2missense = 1 - E**(-media_dominio2missense)
    media_final_dominio2nonsense = 1 - E**(-media_dominio2nonsense)
    
    media_dominio3missense = lmbda * percent['dbd']['missense'] / 100
    media_dominio3nonsense = lmbda * percent['dbd']['nonsense'] / 100
    
    media_final_dominio3missense = 1 - E**(-media_dominio3missense)
    media_final_dominio3nonsense = 1 - E**(-media_dominio3nonsense)

    media_dominio4missense_conservative = lmbda * percent['nls']['missense_conservative'] / 100
    media_dominio4missense_nonconservative = lmbda * percent['nls']['missense_non_conservative'] / 100
    media_dominio4nonsense = lmbda * percent['nls']['nonsense'] / 100
    
    media_final_dominio4missense_conservative = 1 - E**(-media_dominio4missense_conservative)
    media_final_dominio4missense_nonconservative = 1 - E**(-media_dominio4missense_nonconservative)
    media_final_dominio4nonsense = 1 - E**(-media_dominio4nonsense)

    media_dominio5missense = lmbda * percent['od']['missense'] / 100
    media_dominio5nonsense = lmbda * percent['od']['nonsense'] / 100
    
    media_final_dominio5missense = 1 - E**(-media_dominio5missense)
    media_final_dominio5nonsense = 1 - E**(-media_dominio5nonsense)

    media_dominio6missense = lmbda * percent['ctd']['missense'] / 100
    media_dominio6nonsense = lmbda * percent['ctd']['nonsense'] / 100
    
    media_final_dominio6missense = 1 - E**(-media_dominio6missense)
    media_final_dominio6nonsense = 1 - E**(-media_dominio6nonsense)

    return {"dominio1missense": media_final_dominio1missense,
            "dominio1nonsense": media_final_dominio1nonsense,
            "dominio2missense": media_final_dominio2missense,
            "dominio2nonsense": media_final_dominio2nonsense,
            "dominio3missense": media_final_dominio3missense,
            "dominio3nonsense": media_final_dominio3nonsense,
            "dominio4missense_conservative": media_final_dominio4missense_conservative,
            "dominio4missense_non_conservative": media_final_dominio4missense_nonconservative,
            "dominio4nonsense": media_final_dominio4nonsense,
            "dominio5missense": media_final_dominio5missense,
            "dominio5nonsense": media_final_dominio5nonsense,
            "dominio6missense": media_final_dominio6missense,
            "dominio6nonsense": media_final_dominio6nonsense
    }