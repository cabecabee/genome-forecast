# Genome Forecast
    A program designed to receive DNA sequences and simulate mutations based on user habits.

## Overview
**Genome Forecast** estimates how certain lifestyle habits may cause mutations in DNA sequences, helping to evaluate an individual's potential risk of developing cancer.  

Currently, the program is focused on **tobacco use** as a mutagenic factor.

## How it works
1. The user provides one or more DNA sequences in a **FASTA file**.  
2. The program collects user input about their daily habits — such as smoking frequency and intensity.  
3. Based on this data, it estimates the **number and types of mutations** that could occur.  
4. It then simulates these mutations in the provided DNA sequence and classifies them (e.g., **silent**, **missense**, or **nonsense**).  

## Features (Work in Progress)
- [x] User input and data processing  
  - Calculates the estimated number of mutations based on lifestyle data  
- [x] Reading and parsing FASTA files  
  - Extracts ID, description, sequence, and base count  
- [x] Extracting coding regions (codons) from DNA sequences  
- [x] Mutation probability estimation  
  - Uses **weights derived from the COSMIC Cancer Database**  
- [x] DNA sequence mutation simulation  
  - Determines mutation impact: silent, missense, or nonsense

## Future Plans
- [ ] Define what the mutations may signify to the resulting protein structure or function 
