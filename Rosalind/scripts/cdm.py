def distance_matrix(sequence):
  n = len(sequence)
  length = len(sequence[0])
  D = [[0.0 for i in xrange(n)] for j in xrange(n)]
  for i in xrange(n):
    for j in xrange(n):
      if i == j:
        pass
      else:
        dc = 0.0
        for c in xrange(length):
          if sequence[i][c] != sequence[j][c]:
            dc += 1
        D[i][j] = dc/length
  return D
if __name__ == '__main__':
  import Fasta
  fasta = Fasta.FASTA('/home/ycz/Rosalind/input/cdm_in.txt')
  sequence = fasta.sequence()
  D = distance_matrix(sequence)
  with open('/home/ycz/Rosalind/output/cdm_out.txt', 'w+') as output:
    for ind,ite in enumerate(D):
      output.write(' '.join(map(str,ite)) + '\n')
