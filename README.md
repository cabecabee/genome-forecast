# Genome Forecast
    A program designed to receive DNA sequences and simulate mutations to it.

## What exactly does Genome Forecast do?
Genome Forecast will receive one or more DNA sequences, determined in a fasta file, and input from the user, asking for day-to-day habits that could cause cancer, the frequency of those habits, and the intensity. With that information, it will simulate mutations in the DNA sequence and give the user how many mutations their habits could cause, thus giving the user an estimated chance of them developing a tumor. \
The program is currently designed exclusively for smokers.

## Features (WIP)
* Input from the user and the processing of the data given by the user
    * Estimated number of mutations based on the data given
* Reading the FASTA file and separating it into ID, description, sequence and number of bases
* Function to get the codifying codons of the DNA from the FASTA file
* Function to get the probability of mutations happening in each base
    * The probability is calculated using weights provided by the COSMIC Cancer Database
* Mutating a string that represents the DNA sequence
    * Interpreting what the mutation did (i.e. knowing if it is a silent, nonsense or missense mutation)
