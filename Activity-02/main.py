rna = "AUGCCCCUGCGGAGCUCCAGUUCGCCACUAAGAUCUGAAGCUCGCCAGAGACGCCGGUUCUUACAUGUGUCCUCGCCAUCUGUUGAGCCGAGUACUCCCCCCGACCGUGGUACUGGUUCCAUACACCACUUGAUCACUAGCGGGACCCCAACUCGAUCGAUGAAGCAAGAAGAUCAAGCCCACCAACAAGGCGUCGUGAACGUAGAGGACUCUCAACGUGUACUUAAGGCAGUGACGCCAGUGUCAACCACAACCAGUACUACACAAUAUAACGGCUUGAUGUAUAUUUCCCCGCGACACGACUGA"
a =len(rna)
ribosome = ""
count = 0
geneticCode = {
        'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 
        'UCU':'S', 'UCC':'S', 'UCA':'L', 'UCG':'L', 
        'UAU':'Y', 'UAC':'Y', 'UAA':'ST', 'UAG':'ST', 
        'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W', 
        'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
        'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
        'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
        'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
        'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
        'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
        'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
        'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
        'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
        'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
        'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
        'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
        }

# separing genetic codes and comparing
for i in range(len(rna)):
    if count == 2:
        count = 0
        element = ""
        element += rna[i-2] + rna[i-1] + rna[i]
        if element ==  "UAA" or element ==  "UAG" or element ==  "UGA":
            break
        ribosome += geneticCode[element]
    else:
        count += 1

#saving the result in a file
f = open("ribosome.txt", "a")
f.write(ribosome)
f.close()

print("INPUT: ", rna, "\nOUTPUT: ", ribosome)