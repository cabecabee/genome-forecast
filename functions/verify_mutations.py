from dicts.domains import domains
def verify_mutations(mutations):
    # como o analyze mutations já verifica se é nonsense ou missense, podemos simplesmente ver onde ficam as mutações e dar a porcentagem em cada domínio
    return [(pos, mut_type, get_domain(pos)) for pos, mut_type in mutations]

def get_domain(pos): # decidi por colocar a função aqui pois só é usada para realizar o verify_mutations, e não quero poluir a pasta functions mais do que já está
        for name, coords in domains.items():
            if coords["start"] <= pos + 1 <= coords["end"]:
                return name