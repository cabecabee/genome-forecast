from Bio import SeqIO

for record in SeqIO.parse("exemplo.fasta", "fasta"):
    print("Nome:", record.id)       # nome da sequência
    print("Descrição:", record.description)
    print("Sequência:", str(record.seq))