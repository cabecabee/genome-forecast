# Genome Forecast
    A program designed to receive DNA sequences and simulate mutations based on user habits.

## Overview
**Genome Forecast** estimates how certain lifestyle habits may cause mutations in DNA sequences, helping to evaluate an individual's potential risk of developing cancer.  

Currently, the program is focused on **tobacco use** as a mutagenic factor.

At this moment, the program is focused on **portuguese**. It is planned to have english support in the future.

## How it works
1. The user provides one or more DNA sequences in a **FASTA file**.  
2. The program collects user input about their daily habits, such as smoking frequency and intensity.  
3. Based on this data, it estimates the **number and types of mutations** that could occur.  
4. It then simulates these mutations in the provided DNA sequence and classifies them (e.g., **silent**, **missense**, or **nonsense**).  

## Features
- [x] User input and data processing  
  - Calculates the estimated number of mutations based on lifestyle data  
- [x] Reading and parsing FASTA files  
  - Extracts ID, description, sequence, and base count  
- [x] Extracting coding regions (codons) from DNA sequences  
- [x] Mutation probability estimation  
  - Uses **weights derived from the COSMIC Cancer Database**  
- [x] DNA sequence mutation simulation  
  - Determines mutation impact: silent, missense, or nonsense
- [x] Gives a chance of a mutation happening in each domain (and chance of a nonsense mutation)
  - Gives the user context (what a mutation in each domain could mean)
     
## How to Run

### Running the Executable (.exe)
If you downloaded the compiled executable version, simply run it and **follow the on-screen instructions**.  
The program will ask a few questions about your smoking habits which are handled by the `user_data()` function.  
After you answer, it will simulate mutations and display the results directly in the terminal.

---

### Running from Source Code
If you want to run the program from source:

1. Make sure you have **Python 3.10+** installed.
2. Clone or download the repository.
3. Inside the project folder, run:

   ```bash
   python main.py
