for i in range(round(lambida)):
  #escolha da posição
  p_chosen = sorteio_pond(p_cumulative)
  #verifica pesos desta pos
  b_weights = probabilities_mut[p_chosen]["pesos"]

  #cria regua cumulativa local para as mut
  local_cumulative = []
  local_sum = 0
    for base, prob in p_weights.items():
      local_sum += prob
      local_cumulative.append((base, local_sum))

  #sorteia nova base
  n2 = random.random()
  new_base = None
    for base, limit in local_cumulative:
      if n2 <= limite:
          nova_base = base
          break

  #meio ilustrativo, n tem seq_mut e tbm n acho que será desta forma.
  if nova_base:
      seq_mut[p_chosen] = nova_base
