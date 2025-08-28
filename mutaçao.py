import random

taxa_mutacao = 0.01
int = taxa_mutacao

tamanho_sequencia = 120 #Somente para teste
int = tamanho_sequencia

numero_geracoes = random.randint(5, 10)

total_mutacoes = tamanho_sequencia * taxa_mutacao * numero_geracoes

print(f'Total de mutações esperadas: {total_mutacoes}')
print(" ")
print("Numeros:")
print(f'Taxa de mutação: {taxa_mutacao}')
print(f'Tamanho da sequência: {tamanho_sequencia} (teste)')
print(f'Número de gerações: {numero_geracoes}')