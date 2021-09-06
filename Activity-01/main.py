input = "TTCCAGGCGTCATCTCCTATATTCTGGGTCCTCTGGGGTCTGGGTTTGCCTCTGTGTAGTCACGTACATTGACTTTTCATCTGTGATCGCGCAATGAACTTTGTACTACCGACACTCAAGTAGCACACTTGTACAGGAAACAAGTCGGGT"
output = ""

for i in input:
    if i == 'T':
        output += 'U'
    else:
        output += i

f = open("rna.txt", "a")
f.write(output)
f.close()

print("INPUT: ", input, "\nOUTPUT: ", output)
