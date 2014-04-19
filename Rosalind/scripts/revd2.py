def revd(l1,l2):
  reference = dict(zip(l1,range(1,len(l1)+1)))
  trans_seq = [0]
  for i in l2:
    trans_seq.append(reference[i])
  trans_seq.append(len(l1) + 1)
  def exi_decreasing_strip(trans_seq):
    if trans_seq[0] - trans_seq[1] == 1 or (trans_seq[0] - trans_seq[1] != -1 and trans_seq[0] != 0 and trans_seq[0] != len(trans_seq) - 1):
      return True
    for i in xrange(1,len(trans_seq)-1):
      if trans_seq[i+1] - trans_seq[i] == -1 or (trans_seq[i+1] - trans_seq[i] != 1 and trans_seq[i] - trans_seq[i-1] != 1 and trans_seq[i] != 0 and trans_seq[i] != len(trans_seq)-1):
	return True
    else:
      return False
  def bps(trans_seq):
    bp = []
    for i in xrange(len(trans_seq)-1):
      if abs(trans_seq[i+1] - trans_seq[i]) != 1:
	bp.append((i,i+1))
    return bp,len(bp)
  def rev_bp(l,i,j):
    lm = l[:]
    if i != 0:
      lm = lm[:i] + lm[j:i-1:-1] + lm[j+1:]
    else:
      lm = lm[j::-1] + lm[j+1:]
    return lm
  min_bp = 2000
  rt = 0
  #print trans_seq
  import itertools
  while bps(trans_seq)[1] != 0:
    if exi_decreasing_strip(trans_seq):
      for i in itertools.permutations(range(1,len(trans_seq)-1),2):
	if i[0] < i[1]:
	  check = bps(rev_bp(trans_seq,i[0],i[1]))
	  if check[1] < min_bp:
	    rec = (i[0],i[1])
	    min_bp = check[1]
      trans_seq = rev_bp(trans_seq,rec[0],rec[1])[:]
      print rec[0],rec[1]
      #print rec
      #print trans_seq
      #print bps(trans_seq)
      #print min_bp
    else:
      for i in itertools.permutations(bps(trans_seq)[0],2):
	if i[0][1] < i[1][0] and i[0][1] != 0 and i[1][0] != len(trans_seq) - 1:
	  if trans_seq[i[0][1]:i[1][0]+1] == range(trans_seq[i[0][1]],trans_seq[i[0][1]]+i[1][0]-i[0][1]+1):
	    trans_seq = rev_bp(trans_seq,i[0][1],i[1][0])
	    min_bp = bps(trans_seq)[1]
	    #print trans_seq
	    print i[0][1], i[1][0]
	    break
    rt += 1
  #print bps(trans_seq)
  #print reference
  #print trans_seq
  return rt
					     
if __name__ == '__main__':
  init_perms = []
  with open('/home/ycz/Rosalind/input/SORT_in.txt', 'r') as input_data:
    for line in input_data:
      if len(line) != 1:
	linex = line.strip('\n').split(' ')
	init_perms.append(map(int,linex))
  perms = []
  #print init_perms
  #for i in xrange(0,10,2):
  #   print revd(init_perms[i],init_perms[i+1]),
  for i in range(0,2,2):
    print revd(init_perms[i+1],init_perms[i])
  #print revd(range(1,9),[8,2,7,6,5,1,4,3])
