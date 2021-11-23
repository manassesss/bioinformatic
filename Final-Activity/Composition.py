def readFile():
    arquivo = 'input.fasta'
    print("Loading ", arquivo, "...")
    f = open(arquivo, 'r') 
    lines = f.readlines() 
    sequence = ""
    k = ""
    aux = ""
    for line in lines:
        if line.find('>') == 0: 
            line = line.rstrip("\n")
            line = line.split("=")
            k = int(line[1])
            
        else:
            aux += line.rstrip("\n") 
    sequence = aux
    return sequence, k

def montageKmers(sequence, k):
    kmers = []
    for i in range(len(sequence)):
        kmer= sequence[i:i+k]

        if (len(kmer) < k or len(kmer.rstrip("\t")) < k):
            break
        else:
            kmers.append(kmer)
    kmers.sort()
    name = "k" + str(k)+ "mer.txt"
    f = open(name, "w")
    for pair in kmers:
        f.write(pair + ",")
    print("Saving ", name, " ...")
    f.close()
    print("Done!!")
    
def main():
    sequence, k = readFile()
    montageKmers(sequence, k)

if __name__ == "__main__":
    main()