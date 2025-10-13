def user_data():

    tabagism = True
    
    while tabagism :
        print("")
        print("Você tem o hábito do tabagismo?")
        print("1: Sim, costumo fumar com frêquencia")
        print("2: Não, não costumo fumar")

        tabagismo = input("Resposta: ")

        try:
            r_tabagismo = int(tabagismo)
            if tabagismo == "1":
                break
            else:
                print("Resposta incompátivel com a sequência do programa!")
        except:
            print("Resposta inválida")
        
    tabagism = False
            
    intensit = True
    while intensit :
        print("")
        print("Quantos cigarros você fuma por dia, em média?")
        intensity = input("Número de cigarros: ")

        try:
            n_intensity = int(intensity)
            if n_intensity >= 1:
                break
            else:
                print("")
                print("Valor deve ser > 0!")
        except:
            print("A resposta deve ser numérica!")

    intensit = False
            
    habit = True
    while habit:
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
        except:
            print("A resposta deve ser numérica!")

    habit = False
                
    pack = n_intensity / 20
    years = n_period / 12

    packyears = pack * years

    beta = 150 / 1

    L = 1200 * 2
    D = 10
    alfa = beta / (L * D)

    u0 = 1.00e-9
    u =  u0 + (alfa * packyears)

    lambida = u * L * D

    print("Número esperado de mutações:", lambida)


user_data()
