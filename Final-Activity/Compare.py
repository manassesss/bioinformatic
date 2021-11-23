original = open("Topicos.Bioinformatica.sequencia_1_Bioinformaticas_size_50000_k_80.txt", "r").readlines()
falsificado = open("output.fasta", "r").readlines()

print(original == falsificado)