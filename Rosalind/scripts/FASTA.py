#!/usr/bin/env python
#Parsing FASTA files.
class FASTA(object):
    def __init__(self, file_name):
        self.file_name = file_name
    def sequences(self):
        sequences = []
        names = []
        n = -1
        with open(self.file_name,'r') as input_data:
            for line in input_data:
                if line[0] == '>':
                    names.append(line[:-1])
                    n += 1
                    sequences.append("")
                else:
                    sequences[n] = sequences[n] + line.strip('\n\r') #\r is there for no reason.
        return sequences
    def names(self):
        sequences = []
        names = []
        n = -1
        with open(self.file_name,'r') as input_data:
            for line in input_data:
                if line[1] == '>':
                    names.append(line[:-1])
                    n += 1
                    sequences.append('')
                else:
                    sequences[n] = sequences[n] + line.strip('\n')
        return names
