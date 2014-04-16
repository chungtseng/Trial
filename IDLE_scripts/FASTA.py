# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def fasta(file_name):
    """
Put Fasta format files into two arrays: na and se.
Have to add a ">" at the end of the fasta file!
"""
    fasta = open(file_name,"r+")
    #fasta.write(">")
    ff = fasta.read()
    fasta.close()
    se = []
    na= []
    sequence = ""
    name = ""
    memory = ""
    for c in ff:
        if c == ">":
            se.append(sequence)
            na.append(name)
            sequence = ""
            name = ""
            memory = memory + c
        elif c != "\n":
            memory = memory + c
        elif c == "\n":
            for i in memory:
                if i == ">":
                    name = memory
                    memory = ""
                    break
                else:
                    sequence = sequence + memory
                    memory = ""
    se.append(sequence)
    na.append(name)
    del se[0]
    del na[0]
    return [se, na]

# <codecell>

if __name__ == '__main__':
    result = fasta("/home/ycz/Rosalind/mm.txt")
    sequence = result[0]
    name = result[1]
    print result

# <codecell>


