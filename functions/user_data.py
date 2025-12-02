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

        while True:
            print("")
            print("Há quantos anos você fuma?")
            try:
                period_a = int(input("Tempo: ").strip())
                if period_a >= 0:
                    break
                else:
                    print("Resposta deve ser >= 0!")
            except ValueError:
                print("A resposta deve ser em números inteiros!")

        # Pergunta 4
        while True:
            print("")
            print("E quantos meses em cima disso?")
            try:
                period_m = int(input("Tempo: ").strip())
                if period_m >= 0:
                    break
                else:
                    print("Resposta deve ser >= 0!")
            except ValueError:
                print("A resposta deve ser em números inteiros!")

        print("")
        print("Você quer uma previsão para o futuro (1) ou só quer saber uma previsão do momento atual (2)?")
        while True:
            prevdec = input("Resposta (1/2): ").strip()
            if prevdec in ["1", "2"]:
                break
            else:
                print("Resposta inválida! Digite '1' ou '2'.\n")

        if prevdec == "1":
            while True:
                print("")
                print("Para quantos anos você quer essa previsão?")
                try:
                    periodp_a = int(input("Tempo: ").strip())
                    if periodp_a >= 0:
                        break
                    else:
                        print("Resposta deve ser >= 0!")
                except ValueError:
                    print("A resposta deve ser em números inteiros!")

            while True:
                print("")
                print("E quantos meses em cima disso?")
                try:
                    periodp_m = int(input("Tempo: ").strip())
                    if periodp_m >= 0:
                        break
                    else:
                        print("Resposta deve ser >= 0!")
                except ValueError:
                    print("A resposta deve ser em números inteiros!")

            n_period = (period_a * 12 + period_m) + (periodp_a * 12 + periodp_m)

        else:
            n_period = (period_a * 12 + period_m)

        if n_period < 1:
            print("Isto não configura um hábito.")
            return

    except (EOFError, KeyboardInterrupt):
        print("\nPrograma encerrado pelo usuário.")
        return

    pack = n_intensity / 20 #nº de maços
    years = n_period / 12 #transferencia para anos

    packyears = pack * years #medida universal para quantificar tabagismo.

    beta = 5.5e-5 #nº de mutações por uma unidade de exposição em gene da P53 (150 x 3.684375×10−7 = 5,5 × 10⁻⁵).
    D = n_period * 1.8 #quantidade de divisões celulares neste periodo de tempo.
    u0 = 1.00e-9 #taxa basal de mutação
    u = u0 + (beta * packyears) #taxa total de mutação por base e por divisão celular.

    lambida = u * D #número esperado de mutações no gene durante aquele período.

    return lambida, prevdec