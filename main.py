from dicts.dict_sbs4 import dict_sbs4
from dicts.hotspots import hotspots
from functions.duplicate import duplicate
from functions.get_cds import get_cds
from functions.get_weights import get_weights
from functions.isdna import isdna
from functions.mutate import mutate
from functions.poisson import poisson
from functions.prob_mut import prob_mut
from functions.read_fasta import read_fasta
from functions.transcript import transcript
from functions.translate import translate
from functions.user_data import user_data
from functions.mat_mut import mat_mut
from functions.resource_path import resource_path
from functions.sorteio_pond import sorteio_pond
from functions.analyze_mutations import analyze_mutations
from functions.repeat_mutations import repeat_mutations
from functions.scale import normalize
from functions.scale import calculate_risk
from functions.pelomenosum import pelomenosum
import os
import sys
import re

from tkinter import Tk # interface gráfica para escolher um arquivo fasta
from tkinter.filedialog import askopenfilename

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    usecustomfasta = input(
        "Você gostaria de usar um arquivo FASTA personalizado (por exemplo, da sua própria TP53)?\n"
        "(Note que esse arquivo FASTA deve estar em bases nitrogenadas de DNA e não codificado.)\n"
        "Se você não fornecer, será usado o FASTA padrão da TP53 obtido no banco de dados NCBI (National Library of Medicine).\n"
        "Digite 'S' para Sim ou 'N' para Não: "
    ).strip().lower()

    if usecustomfasta in ["s", "n"]:
        break
    else:
        print("Resposta inválida! Digite 'S' ou 'N'.\n")

if usecustomfasta == "s":
    root = Tk()
    root.withdraw() # esconde a janela do tkinter que é inútil para nós no momento
    filepath = askopenfilename(
        title="Selecione o arquivo FASTA",
        filetypes=[
            ("FASTA files", "*.fasta"),
            ("FASTA Nucleotide", "*.fna"),
            ("FASTA Fragments", "*.ffn"),
            ("FASTA short", "*.fa"),
            ("FASTA alternate", "*.fas")
        ]
    )
    root.destroy()  # fecha a instância Tk após selecionar o arquivo
    if filepath:
        print("Arquivo selecionado:", filepath)
    else:
        print("Nenhum arquivo selecionado. Usando o FASTA da NCBI por padrão.")
        filepath = resource_path("fastafiles/p53.fasta")
elif usecustomfasta == "n":
    filepath = resource_path("fastafiles/p53.fasta")

lmbda, prevdec = user_data()

if lmbda is None or lmbda == 0:
    input("\nPrograma finalizado. Pressione ENTER para sair...")
    sys.exit()

try:
    seq = "".join(i["seq"] for i in read_fasta(filepath))
except Exception:
    print("Erro: o arquivo selecionado não é um FASTA válido.")
    input("\nPrograma finalizado. Pressione ENTER para sair...")
    sys.exit()

p_cumulative, probabilities_mut = prob_mut(seq)

pelomenosumtabela = pelomenosum(lmbda, seq, p_cumulative, probabilities_mut, 113000)

for k in pelomenosumtabela:
    pelomenosumtabela[k] *= 100
nonsense_total = sum(
    value for key, value in pelomenosumtabela.items()
    if "nonsense" in key
)
clear_terminal()
print("=======================================================================\n")

descricao_dominios = {
    "Domínio 1 (TAD)": "uma perda na capacidade de recrutar genes que executam o reparo e controlam o ciclo celular. Ou seja, quando uma região como essa é danificada,\n"
    "ocorre a dificuldade de recrutar proteínas necessárias para iniciar a transcrição, e,\n"
    "consequentemente, a célula continua em divisão mesmo sem ativar adequadamente os meios corretores.\n"
    "• Com o tempo, a junção da divisão contínua e do reparo insuficiente favorece a instabilidade genética, facilitando o\n"
    "surgimento de mutações adicionais e contribuindo para a evolução de fenótipos malignos.\n",

    "Domínio 2 (PRD)": "falha parcial na capacidade da p53 de recrutar proteínas de reparo. Neste sentido,\n"
    "a p53 passa a ter dificuldades na ativação de proteínas pró-apoptóticas cruciais,\n"
    "reduzindo a eficiência com que a célula elimina estruturas comprometidas.\n"
    "Como consequência, células que deveriam ser removidas permanecem em atividade.\n"
    "• Esse acúmulo de células mutadas favorece a concentração de alterações genéticas e impulsiona a evolução de células danosas.\n",

    "Domínio 3 (DBD)": "redução da capacidade de ligação ao DNA. Com isso, a estrutura do sítio de ligação é alterada,\n"
    "impedindo a p53 de ativar genes responsáveis por interromper o ciclo celular,indutores de reparo ou à apoptose. Sem essa ligação,\n"
    "a regulação que depende da p53 é diretamente comprometida.\n"
    "• A partir disso, a ausência dessa regulação permite que danos induzidos se acumulem descontroladamente,\n"
    "desestabilizando o genoma e acelerando o surgimento de mutações que estimulam a progressão neoplásica.\n",

    "Domínio 4 (NLS)": "dificuldade em transportar a p53 para o núcleo da célula.\n"
    "Dessa forma, a proteína passa a apresentar dificuldade em ser reconhecida pelos mecanismos de transporte do núcleo,\n"
    "permanecendo em grande parte ou por completo no citoplasma. Consequentemente, a p53 deixa de se comunicar com o DNA,\n"
    "o que impede a ativação de genes relevantes como os citados anteriormente.\n"
    "• Logo, essa falha da “inserção” da p53 no DNA reduz drasticamente o potencial de vigilância genômica,\n"
    "favorecendo a permanência de danos não corrigidos nas células.\n",

    "Domínio 5 (OD)": "problemas na formação do tetrâmetro funcional da p53. Quando isso ocorre, a proteína se torna incapaz de assumir sua forma funcional,\n"
    "resultando em complexos instáveis e mal formados, impedindo que a p53 execute sua função de forma eficaz,\n"
    "mesmo quando outras regiões permanecem estruturadas.\n"
    "• Portanto, a insuficiência de tetramerização compromete profundamente a resposta ao dano celular,\n"
    "permitindo que células danificadas persistam e se dividam, o que favorece o aumento de alterações genômicas.\n",

    "Domínio 6 (CTD)": "alterações na regulação fina e reconhecimento de DNA danificado. Isto é,\n"
    "a proteína passa a ter dificuldade em reconhecer regiões prejudicadas do DNA e\n"
    "em receber modificações químicas que modulam sua ativação.\n"
    "• Como resultado, a p53 responde de maneira insuficiente ou tardia aos sinais de estresse genômico. E, com o tempo,\n"
    "essa resposta ineficiente permite que danos se acumulem sem a correção necessária,\n"
    "ampliando a instabilidade genética e contribuindo para a formação de células com características possivelmente oncogênicas.\n"
}

dominios = {
    "Domínio 1 (TAD)": ["dominio1missense", "dominio1nonsense"],
    "Domínio 2 (PRD)": ["dominio2missense", "dominio2nonsense"],
    "Domínio 3 (DBD)": ["dominio3missense", "dominio3nonsense"],
    "Domínio 4 (NLS)": ["dominio4missense_conservative", "dominio4missense_non_conservative", "dominio4nonsense"],
    "Domínio 5 (OD)": ["dominio5missense", "dominio5nonsense"],
    "Domínio 6 (CTD)": ["dominio6missense", "dominio6nonsense"]
}

risco_por_dominio = {}

for nome, keys in dominios.items():
    soma = sum(pelomenosumtabela.get(k, 0) for k in keys)
    risco_por_dominio[nome] = soma

for nome, risco in risco_por_dominio.items():
    dano = descricao_dominios.get(nome, "alteração funcional")
    print(f"-> {nome}: {risco:.3f}% de chance de apresentar {dano}")
print()

print("=======================================================================\n")

print(f"Chance de uma mutação que interrompe completamente a função da p53 (mutações nonsense): {nonsense_total:.3f}%")

print("""
Essas mutações costumam gerar uma proteína p53 truncada, que perde a capacidade de:

• Reparar DNA danificado  
• Parar o ciclo celular para evitar replicação defeituosa  
• Induzir apoptose (“morte celular programada”) quando necessário  

Em outras palavras, mutações nonsense estão fortemente associadas à perda total do papel da p53 como supressora tumoral.
""")

print("=======================================================================\n")

print("As porcentagens acima representam a CHANCE ABSOLUTA de ocorrer pelo menos\n"
      "uma mutação em cada domínio, considerando a exposição informada.\n"
      "Esses valores NÃO somam 100%, pois cada domínio é independente.\n")

print("=======================================================================\n")

# print("Com isso, constata-se um risco ()\n")

# print("=======================================================================\n")

print("De qualquer forma, denota-se que este hábito é maléfico e tem potencial de \n" \
"causar câncer em qualquer quantidade.")

input("\nPrograma finalizado. Pressione ENTER para sair...")

'''  
███████████████████████████████████████████████████
██████████████   ██████████████████████████████████
███████████████    ████████████████████████████████
█████████████  ██   ███████████████████████████████
███████████  █████  ███████████████████████████████
████████   █████    ███████████████████████████████
███  █   █████   █  ███████████████████████████████
█████   ████   ██   ███████████████████████████████
████████                    ███████████████████████
█████████████████  ████   █    ████████████████████
████████████████  ███   █████    ██████████████████
████████████████      ████   ██   █████████████████
█████████████████   ████   ████   █████████████████
█████████████████   ██   ████     █████████████████
███████████████████    ████   ██  █████████████████
█████████████████████                    ██████████
██████████████████████████████   ████       ███████
███████████████████████████████  ██   █████    ████
██████████████████████████████      █████  ███  ███
███████████████████████████████   █████  ██████████
████████████████████████████████  ███  ████████████
█████████████████████████████████    ██████████████
██████████████████████████████████   ██████████████
███████████████████████████████████████████████████
'''