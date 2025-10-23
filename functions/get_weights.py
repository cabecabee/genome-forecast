import math
hotspots = {
    175*3: 8.0, # VALOR ARBITRARIO, MUDAR DEPOIS! (o peso, não o hotspot!)
    248*3: 12.0, # IDEM
    273*3: 15.0 # IDEM
}
def get_weights(seq):
    weights = [1.0 for _ in seq]
    for h, pico in hotspots.items():
        for i in range(max(0, h - 15), min(len(weights), h + 15)):
            distancia = abs(i - h)
            peso = 1 + (pico - 1) * math.exp(- (distancia ** 2) / (2 * (8 ** 2)))
            weights[i] = max(weights[i], peso)
    return weights
