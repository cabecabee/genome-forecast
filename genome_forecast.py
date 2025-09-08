print("Bem vindo ao programa Genome Forecast!")
print('Utilize a seguinte sintaxe: "1 3" caso tenha, por exemplo, os hábitos 1 e 3. Caso tenha apenas um, apenas digite o número deste hábito.')

print("")
print("Indique quais destes hábitos você tem:")
print("1: Exposição ao sol")
print("2: Má alimentação")
print("3: Tabagismo")
print("")

habitos = input("Hábito(s): ").split()

print("")
print("Perfeito! Com qual intensidade (tempo no dia) você realiza estes hábitos?")
print("1: Leve")
print("2: Moderada")
print("3: Alta")
print("")

intensidade = str(input("Intensidade: "))

print("")
print("Finalmente, o quão frequentemente na semana você realiza estes hábitos?")
print("1: 1-2 vezes")
print("2: 3-5 vezes")
print("3: 6-7 vezes")
print("")

periodo = str(input("Periodicidade: "))