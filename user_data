from functions.mutate import mutate
from functions.read_fasta import read_fasta

print("Bem vindo ao programa Genome Forecast!")
print("Forneça respostas somente númericas")

print("")
print("Você tem o hábito do tabagismo?")
print("1: Sim, costumo fumar com frêquencia")
print("2: Não, não costumo fumar")

tabagismo = input("Resposta: ")

if tabagismo == "2":
    print("Infelizmente, não será possível utilizar o Genome Forecast neste caso!")
else: 
    print("")
    print("Quantos cigarros você fuma por dia, em média?")
    intensity = int(input("Número de cigarros: "))

    if intensity < 1:
        print("")
        print("Valor inválido")
    else:
        print("")
        print("Há quanto tempo você fuma em meses?")
        period = int(input("Tempo em meses: "))
        print("")

        if period < 1:
            print("Isto não configura um hábito.")
        else:
    
        pack = intensity / 20
        years = period / 12

        packyears = pack * years
