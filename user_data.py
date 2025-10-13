def user_data():

    tabagism = True
    
    while tabagism :
        print("")
        print("Você tem o hábito do tabagismo?")
        print("1: Sim, costumo fumar com frêquencia")
        print("2: Não, não costumo fumar")

        tabagismo = input("Resposta: ")

        if tabagismo == "2":
            print("Infelizmente, não será possível utilizar o Genome Forecast neste caso!")
        elif tabagismo != "1":
            print("Resposta inválida")
        else:
            tabagism = False
            intensit = True
            while intensit :
                print("")
                print("Quantos cigarros você fuma por dia, em média?")
                intensity = int(input("Número de cigarros: "))

                if intensity < 1 or not isinstance(intensity, int):
                    print("")
                    print("Valor inválido")
                else:
                    intensit = False
                    habit = True
                    while habit:
                        print("")
                        print("Há quanto tempo você fuma em meses?")
                        period = int(input("Tempo em meses: "))
                        print("")

                        if period < 1 or not isinstance(period, int):
                            print("Isto não configura um hábito.")
                        else:
                
                            pack = intensity / 20
                            years = period / 12

                            packyears = pack * years

                            beta = 150 / 1

                            L = 1200 * 2
                            D = 10
                            alfa = beta / (L * D)

                            u0 = 1.00e-9
                            u =  u0 + (alfa * packyears)

                            lambida = u * L * D

                            print(packyears)
                            print("Número esperado de mutações:", lambida)

                            habit = False
