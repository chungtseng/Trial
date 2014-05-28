#!/usr/bin/env python
#Parsing FASTA files.
class FASTA(object):
	def __init__(self, file_name):
		self.file_name = file_name
		self.fasta = open(self.file_name,"r").read()
	def sequence(self):
		    se = []
		    na = []
		    sequence = ""
		    name = ""
		    memory = ""
		    for c in self.fasta:
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
		    return se
	def name(self):
		    se = []
		    na = []
		    sequence = ""
		    name = ""
		    memory = ""
		    for c in self.fasta:
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
		    return na
