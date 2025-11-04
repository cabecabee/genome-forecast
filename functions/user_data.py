def user_data():
    try:
        # Pergunta 1
        while True:
            print("")
            print("Você tem o hábito do tabagismo?")
            print("1: Sim, costumo fumar com frequência")
            print("2: Não, não costumo fumar")

            tabagismo = input("Resposta: ").strip()

            if tabagismo == "1":
                break
            elif tabagismo == "2":
                print("\nComo você não é fumante, este cálculo não se aplica.")
                return
            else:
                print("Resposta incompatível! Digite 1 ou 2.")

        # Pergunta 2
        while True:
            print("")
            print("Quantos cigarros você fuma por dia, em média?")
            intensity = input("Número de cigarros: ")

            try:
                n_intensity = int(intensity)
                if n_intensity >= 1:
                    break
                else:
                    print("Resposta deve ser > 0!")
            except ValueError:
                print("A resposta deve ser em número(s) inteiro(s)!")

        # Pergunta 3
        while True:
            print("")
            print("Há quanto tempo você fuma em meses?")
            period = input("Tempo em meses: ")
            print("")

            try:
                n_period = int(period)
                if n_period >= 1:
                    break
                else:
                    print("Isto não configura um hábito.")
            except ValueError:
                print("A resposta deve ser em número(s) inteiro(s)!")
    except (EOFError, KeyboardInterrupt):
            print("\nPrograma encerrado pelo usuário.")
            return
                
    pack = n_intensity / 20 #nº de maços
    years = n_period / 12 #transferencia para anos

    packyears = pack * years #medida universal para quantificar tabagismo.

    beta = 0.000055 #nº de mutações por uma unidade de exposição em gene da P53 (150 x 3.684375×10−7 = 5,5 × 10⁻⁵).

    L = 1179 #tamanho em pb da cds do RNAm da P53alfa.
    D = n_period * 1.2 #quantidade de divisões celulares neste periodo de tempo.
    alfa = beta / (L * D) #umento da taxa por pack-year em mutações por bp por divisão por pack-year.

    u0 = 1.00e-9 #taxa basal de mutação
    u =  u0 + (alfa * packyears) #taxa total de mutação por base e por divisão celular.

    lambida = u * L * D #número esperado de mutações no gene durante aquele período.

    print("Taxa total de mutação por base e por divisão celular:", u)
    print("Número esperado de mutações:", lambida)

    # todos os valores atribuidos diretamente a uma varíavel acima, provêm de dados totalmente cíentificos.
    return lambida

# Alta complexidade para evitar exceções pois essa parte do programa depende do usuário,
# Logo é de extrema importância que não deixemos o usuário cometer erros que inutilizem o programa.
