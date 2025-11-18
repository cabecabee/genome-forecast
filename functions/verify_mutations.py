from dicts.domains import domains

def verify_mutations(mutations):
    # aqui a função vai retornar um dict contendo o dominio e a quantidade de mutações missense e nonsense nele
    counts = {
        domain: {"missense": 0, "nonsense": 0}
        for domain in domains.keys()
    }

    for pos, mut_type in mutations:
        domain = get_domain(pos)
        if domain is not None:
            counts[domain][mut_type] += 1

    return counts

def get_domain(pos): # decidi por colocar a função aqui pois só é usada para realizar o verify_mutations, e não quero poluir a pasta functions mais do que já está
        for name, coords in domains.items():
            if coords["start"] <= pos + 1 <= coords["end"]:
                return name
        return None