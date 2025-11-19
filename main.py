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
import sys

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

seq = ""
for i in read_fasta(filepath):
    seq += i["seq"]
p_cumulative, probabilities_mut = prob_mut(seq)

domaintable = repeat_mutations(lmbda, seq, p_cumulative, probabilities_mut, 10000)

soma = sum(
    count
    for domain in domaintable.values()
    for count in domain.values()
)

percent = {
    domain: {mut_type: (count / soma) * 100 for mut_type, count in subdict.items()}
    for domain, subdict in domaintable.items()
}

if prevdec == '1':
    header = "Levando em consideração o tempo de previsão que você selecionou, estima-se que o seu DNA apresenta:"
else:
    header = "No momento atual, estima-se que o seu DNA apresenta:"

print(f"""
{header}

{percent['tad']['missense']:.3f}% das mutações foram missense no domínio TAD e
{percent['tad']['nonsense']:.3f}% foram nonsense no domínio TAD.

{percent['prd']['missense']:.3f}% foram missense no domínio PRD e
{percent['prd']['nonsense']:.3f}% foram nonsense no domínio PRD.

{percent['dbd']['missense']:.3f}% foram missense no domínio DBD e
{percent['dbd']['nonsense']:.3f}% foram nonsense no domínio DBD.

{percent['nls']['missense']:.3f}% foram missense no domínio NLS e
{percent['nls']['nonsense']:.3f}% foram nonsense no domínio NLS.

{percent['od']['missense']:.3f}% foram missense no domínio OD e
{percent['od']['nonsense']:.3f}% foram nonsense no domínio OD.

{percent['ctd']['missense']:.3f}% foram missense no domínio CTD e
{percent['ctd']['nonsense']:.3f}% foram nonsense no domínio CTD.
""")

# for i, original, mutated in result["amino_diffs"]:
#     if mutated == "stop":
#         mut_type = "nonsense"
#     elif original != mutated:
#         mut_type = "missense"
#     else:
#         mut_type = "sinônima"
#     print(f"Aminoácido {i}: {original} -> {mutated} ({mut_type})")

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