from functions.read_fasta import read_fasta
from functions.mutate_sequence import mutate_sequence

''''Pois então. Essa função agora vai ser COMPLETAMENTE reformulada.
Não queremos mais só adquirir a taxa de mutações, mas sim
saber ONDE essas mutações acontecem e que essas mutações
sejam aplicadas na duplicata da p53.'''

def mutate(mutationrate, fastafile):
    '''Forma de realizar as mutações:
        1. Ler o arquivo e armazenar seu conteúdo em uma única string.
        2. Aplicar as mutações sobre essa string, de acordo com a taxa de mutação.
        3. Escrever o resultado de volta no arquivo, substituindo o conteúdo 
           da duplicata pela string modificada.'''
    with open(fastafile.replace("fastafiles", "duplicates"), "w") as file:
        for entry in read_fasta(fastafile):
            header = entry["desc"]
            seq = entry["seq"]

            mutated_seq = mutate_sequence(seq, mutationrate)
            #função mutate_sequence é onde vai acontecer a mutação real do arquivo, aqui na função mutate estamos apenas escrevendo para o arquivo

            file.write(f">{header}\n")
            file.write(mutated_seq + "\n")