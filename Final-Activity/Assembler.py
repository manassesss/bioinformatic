from Composition import readFile
from collections import defaultdict


class Assembler():
    def __init__(self, kmers, k):
        self.kmers = kmers
        self.k = k
        self.graphMontage()

    def graphMontage(self):
        self.graph = []
        self.edges = {}
        self.adjacencyList = defaultdict(list)
        self.adjacencyEdge = {}

        for kmer in self.kmers:
            origin = kmer[0:self.k-1]
            edge = kmer
            final = kmer[1:self.k]
            node = (origin, edge, final)
            self.graph.append(node)
            self.adjacencyList[origin].append(final)
            self.adjacencyEdge[origin + final] = edge

    def eulerianPathj(self):

        self.isEulerianPath = False

        self.in_rate, self.out_rate = {}, {}

        for key_v in self.adjacencyList:
            self.in_rate[key_v], self.out_rate[key_v] = 0, 0
            v_list = self.adjacencyList[key_v]
            for v in v_list:
                self.in_rate[v], self.out_rate[v] = 0, 0

        for key_v in self.adjacencyList:
            neighbor_list = self.adjacencyList[key_v]
            self.out_rate[key_v] = len(neighbor_list)
            for neighbor in neighbor_list:
                self.in_rate[neighbor] += 1

        same_rate = True
        amount_differents_v = 0
        differents_v_rate = []

        for v in self.in_rate:
            if(self.in_rate[v] != self.out_rate[v]):
                same_rate = False
                if (amount_differents_v > 2):
                    break
                else:
                    differents_v_rate.append(v)
                    amount_differents_v += 1

        v_start = ""

        if (same_rate == True):
            self.isEulerianPath = True
            if (len(self.in_rate) > 0):
                v_start = self.in_rate.keys()[0]
            else:
                v_start = self.out_rate.keys()[0]
        else:
            if(amount_differents_v == 2):
                v1, v2 = differents_v_rate[0], differents_v_rate[1]
                if ((self.out_rate[v1] + self.in_rate[v1]) == 1) and \
                        ((self.in_rate[v2] + self.out_rate[v2]) == 1):
                    self.isEulerianPath = True
                    if(self.out_rate[v1] > self.in_rate[v1]):
                        v_start = v1[:]
                    else:
                        v_start = v2[:]
        if self.isEulerianPath == True:
            stack, self.path = [], []
            v_chain = v_start

            while(True):
                if (self.out_rate[v_chain] == 0 and len(stack) == 0):
                    break
                else:
                    if self.out_rate[v_chain] == 0:
                        self.path.append(v_chain)
                        v_chain = stack.pop()
                    else:
                        stack.append(v_chain)
                        neighbor = self.adjacencyList[v_chain].pop()
                        self.out_rate[v_chain] -= 1
                        self.in_rate[v_chain] -= 1
                        v_chain = neighbor[:]

            self.path.append(v_start)
            self.path = self.path[::-1]

            eulerian_path = v_start[:]
            eulerian_path_size = len(self.path)
            for i in range(1, eulerian_path_size - 1):
                eulerian_path += " -> " + self.path[i]
            eulerian_path += " -> " + self.path[eulerian_path_size - 1]
        self.rebuildGen()

    def rebuildGen(self):
        edges, eulerian_path_size = [], len(self.path)

        for i in range(eulerian_path_size):
            if(i < eulerian_path_size - 1):
                key = self.path[i] + self.path[i + 1]
                edges.append(self.adjacencyEdge[key])

        edges_size = len(edges)
        self.sequence = edges[0]

        sufixes = ''

        for i in range(1, edges_size):
            sufixes += edges[i][-1]

        self.sequence += sufixes
        
        name = "output.fasta"
        f = open(name, "w")
        f.write(self.sequence)
        print("Saving ", name, " ...")
        f.close()

    def printaAtributos(self):
        print(self.adjacencyList)

    def isEulerian(self):
        return self.isEulerian


def takeKmers(path):
    f = open(path, 'r')
    lines = f.readlines()
    kmers = []

    for line in lines:
        l = line.split(",")
        l.pop()
        for i in l:
            kmers.append(i)
    return kmers


def main():
    _, k = readFile()
    kmers = takeKmers("k" + str(k) + "mer.txt")
    graph = Assembler(kmers, k)
    graph.eulerianPathj()


if __name__ == "__main__":
    main()
