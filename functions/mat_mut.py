from functions.sorteio_pond import sorteio_pond
import random
def mat_mut(lambida, p_cumulative, probabilities_mut):
  mutate = []
  for i in range(round(lambida)):
    #escolha da posição
    p_chosen = sorteio_pond(p_cumulative)
    #verifica pesos desta pos
    b_weights = probabilities_mut[p_chosen]["pesos"]

    #cria regua cumulativa local para as mut
    local_cumulative = []
    local_sum = 0
    for base, prob in b_weights.items():
      local_sum += prob
      local_cumulative.append((base, local_sum))

    #sorteia nova base
    n2 = random.random()
    new_base = None
    for base, limit in local_cumulative:
      if n2 <= limit:
        new_base = base
        break
        
    if new_base:
            mutar.append((probabilities_mut[p_chosen]["pos"], new_base))
      
  return mutate
