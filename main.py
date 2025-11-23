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
import sys
import re

from tkinter import Tk # interface gráfica para escolher um arquivo fasta
from tkinter.filedialog import askopenfilename

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

pelomenosumtabela = pelomenosum(lmbda, seq, p_cumulative, probabilities_mut)
domaintable = repeat_mutations(lmbda, seq, p_cumulative, probabilities_mut)

for k in pelomenosumtabela:
    pelomenosumtabela[k] *= 100

print("As porcentagens abaixo representam a CHANCE ABSOLUTA de ocorrer pelo menos\n"
      "uma mutação em cada domínio, considerando a exposição informada.\n"
      "Esses valores NÃO somam 100%, pois cada domínio é independente.\n")

dominios = {
    "Domínio 1 (TAD)": ["dominio1missense", "dominio1nonsense"],
    "Domínio 2 (PRD)": ["dominio2missense", "dominio2nonsense"],
    "Domínio 3 (DBD)": ["dominio3missense", "dominio3nonsense"],
    "Domínio 4 (NLS)": ["dominio4missense_conservative", "dominio4missense_non_conservative", "dominio4nonsense"],
    "Domínio 5 (OD)": ["dominio5missense", "dominio5nonsense"],
    "Domínio 6 (CTD)": ["dominio6missense", "dominio6nonsense"]
}

for nome, keys in dominios.items():
    print(f"--- {nome} ---")
    for k in keys:
        valor = pelomenosumtabela.get(k, None)
        if valor is not None:

            label = re.sub(r"^dominio\d+", "", k)

            label = label.replace("missense_conservative", "missense conservativa")
            label = label.replace("missense_non_conservative", "missense não conservativa")

            label = label.replace("_", " ").capitalize()

            print(f"{label}: {valor:.3f}%")
    print()

print("=======================================================================\n")

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