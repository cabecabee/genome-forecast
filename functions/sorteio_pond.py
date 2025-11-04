import random

def sorteio_pond(p_cumulative):
  
  n = random.random()
  
  for i, limit in enumerate(p_cumulative):
    if n <= limit:
      return i
  return len(p_cumulative)
    
