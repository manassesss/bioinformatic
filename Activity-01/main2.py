dna = "CTCCCGTAAGTCGATACGTAATGACTCTTGTTCACCATGCTTACGTCGTAAGTCAAGGTAAAAACTGGTAATCCGGATTTGTATTAATTGAAATTTCGTCAACATGACACGAAACACGGCGACTGGGTTGTGTCACTCCAGTGATGGGCGTACTCCGTCTATGGAATGGATGACAGCTGTCAAAAAAGTGGCCATTGCCGGCGATATATCTTCATTCAGGTACGTAAATGCCTGGTTGATGTACCAATTTGTGGATAATCCGATGATTCCCGCTAGTCGTGAATACCTGTTTACTATTAAACGGTCGATAGATCAGTTACGCTGCGGGTGTGAGTGCTGGGCTCTAGGTGGTTACAACAATTCGGAGATATCTTAAGATTTGAATACCTCTGCAGTATCCGGGGGAGACCTGGCAGATACTTAGAACCCCCAGTTGTACCAGTTGTGCAAGACATGCTCAAGCACTACCGATGAGCGTGTCCTGCCACTCATTAACGTATCCATCGAAGCGGAAGGCGCACAGAGTGTGCACTCTCTATACTTGTGTGCAAGCGAGTTTTACGTATAACCTTCAAGCCACAAGCCCCCCAACCGCCCTTATCCTGCGAAGAGACGTCCTTAGAAACGCGTGAGGCTGGTATCGCTCGATGATTACGTCATAGAACTCGTGATCGAATTATCTCGCACGTTGGGATATCCCAGTCCATTCGGGTGAACCTTCACCTTATTCTTTATTCGACGCGTCGGGAAGGCCCCATGTAGACTTAGCGACTCTTTGAAGATGTCATATAAAGATGAGCAACCTTCCGCCTACAGCCCCACCACAGTCGGTCCACACCCACAGGTTTATGGGCTAGCTACACGAATGAATCGTGAGCGTTCACTAGACCATACAGCTTTTAGCGGAAGCGAGATAACTAAAGGGAAGGCTGCAGGATTGGCGCCGTGTGAAAATTCTGGGGGTAGCGCGGTCACCGCCCCACTCTTGCTCTTTCTCCCTATCCCAAACAACGACACGGGCTATCACCAGGGGACATGTCTGGGTTAACCTCAGGTGTTCCGTCCTTTGTGGCACATGTCAATTGAATCTGCCCCGGCGGCAACTGTGAGCATGAATTCTGTCAGTATGTTCGCTTATGTTACGTACGTCTACTACATGCTCTGGAGCACAGGCCTCCTGGTAATAGCAAAAGTCGGCTAGATTACTAGGACCAGATAGAATAAGAAGCCGAATAACGCGTTACCCCTCATCACTGCGGAGTTTAGGTATAAGTCTTATCCTTCAGCCCAGGATACTACATGGGGAAGCAACGCCATTAGCCGGTAATTGCTCCGGGCTTTCTTAATCTCGCATGCAGGGAACAGTGAAGTCCGGTACCTACAAATACAGTCTGCCAGGTCTCTAAGTGAAGAGTAGCCGAGGATCGCTGACAACAAATCCCCGTCGGATATCTCAGTACTCCCCACTGCGTTCGTCTTATTCCGACGTTCCCCTACTGT"
mold = ""
rna = ""

# doing the mold to transcribe
for protain in dna:
    if protain == "T":
        mold += "A"
    elif protain == "A":
        mold += "T"
    elif protain == "G":
        mold += "C"
    elif protain == "C":
        mold += "G"

# transcribing
for protain in range(len(dna)):
    if dna[protain] == "A" and mold[protain] == "T":
        rna += "A"
    if dna[protain] == "T" and mold[protain] == "A":
        rna += "U"
    if dna[protain] == "C" and mold[protain] == "G":
        rna += "C"
    if dna[protain] == "G" and mold[protain] == "C":
        rna += "G"

#saving the result in a file
f = open("rna.txt", "a")
f.write(rna)
f.close()


print("INPUT: ", dna, "\nOUTPUT: ", rna)