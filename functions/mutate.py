import os
from functions.read_fasta import read_fasta
from functions.mat_mut import mat_mut
from functions.duplicate import duplicate

def mutate(lambida, fastafile, p_cumulative, probabilities_mut):
    dstdir = "duplicates"

    # garante que estamos trabalhando com a cópia em "duplicates/"
    if not fastafile.startswith("duplicates/"):
        duplicate(fastafile, dstdir)
        fastafile = os.path.join(dstdir, os.path.basename(fastafile))

    for entry in read_fasta(fastafile):
        header = entry["desc"]
        seq = list(entry["seq"])
        seq_length = len(seq)

        # sorteia e aplica mutações
        mutacoes = mat_mut(lambida, p_cumulative, probabilities_mut)
        for pos, nova_base in mutacoes:
            if 0 <= pos < seq_length:
                seq[pos] = nova_base
            elif 1 <= pos <= seq_length:
                seq[pos - 1] = nova_base

        mutated_seq = "".join(seq)

        # divide a sequência em linhas de até 70 caracteres
        fasta_formatted = "\n".join(
            mutated_seq[i:i+70] for i in range(0, len(mutated_seq), 70)
        )

        # sobrescreve a cópia com a versão mutada
        with open(fastafile, "w") as file:
            file.write(f">{header}\n")
            file.write(fasta_formatted + "\n")

    print(f"Arquivo mutado salvo em: {fastafile}")