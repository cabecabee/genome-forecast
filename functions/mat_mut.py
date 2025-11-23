from functions.sorteio_pond import sorteio_pond
import random
def mat_mut(lambida, p_cumulative, substitution_probs):
  
  if lambida > 1:
     mat_mut_lmbda = lambida
  else:
     mat_mut_lmbda = 1

  mutate = []
  for i in range(round(mat_mut_lmbda)):
    #escolha da posição
    p_chosen = sorteio_pond(p_cumulative)
    #verifica pesos desta pos
    b_weights = substitution_probs[p_chosen]["probs"]

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
            mutate.append((substitution_probs[p_chosen]["pos"], new_base))
      
  return mutate
