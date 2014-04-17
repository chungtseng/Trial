def revd(l1,l2):
  reference = dict(zip(l1,range(len(l1))))
  mess = []
  for i in l2:
    mess.append(reference[i])
  def exi_decreasing_strip(mess):
    if mess[0] - mess[1] == 1 or (mess[0] - mess[1] != -1 and mess[0] != 0 and mess[0] != len(mess) - 1):
      return True
    for i in xrange(1,len(mess)-1):
      if mess[i+1] - mess[i] == -1 or (mess[i+1] - mess[i] != 1 and mess[i] - mess[i-1] != 1 and mess[i] != 0 and mess[i] != len(mess)-1):
	return True
    else:
      return False
  def bps(mess):
    bp = []
    for i in xrange(len(mess)-1):
      if abs(mess[i+1] - mess[i]) != 1:
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
  #print mess
  import itertools
  while bps(mess)[1] != 0:
    if exi_decreasing_strip(mess):
      for i in itertools.permutations(bps(mess)[0]+[(len(mess)-1,0),(0,len(mess)-1)],2):
	if i[0][1] < i[1][0]:
	  check = bps(rev_bp(mess,i[0][1],i[1][0]))
	  if check[1] < min_bp:
	    rec = (i[0][1],i[1][0])
	    min_bp = check[1]
      mess = rev_bp(mess,rec[0],rec[1])[:]
      #print rec
      print mess
      #print bps(mess)
      #print min_bp
    else:
      for i in itertools.permutations(bps(mess)[0]+[(len(mess)-1,0),(0,len(mess)-1)],2):
	if i[0][1] < i[1][0]:
	  if mess[i[0][1]:i[1][0]+1] == range(mess[i[0][1]],mess[i[1][0]]+1):
	    mess = rev_bp(mess,i[0][1],i[1][0])
	    min_bp = bps(mess)[1]
	    break
    rt += 1
    if mess == range(9,-1,-1):
      rt += 1
  #print bps(mess)
  #print reference
  #print mess
  return rt
					     
if __name__ == '__main__':
  init_perms = []
  with open('/home/ycz/Rosalind/input/revd.txt', 'r') as input_data:
    for line in input_data:
      if len(line) != 1:
	linex = line.strip('\n').split(' ')
	init_perms.append(map(int,linex))
  perms = []
  #print init_perms
  #for i in xrange(0,10,2):
 #   print revd(init_perms[i],init_perms[i+1]),
  for i in range(0,10,2):
    print revd(init_perms[i],init_perms[i+1])
  #reference = dict(zip(init_perms[0],range(len(init_perms[0]))))
  #mess = []
 # for i in init_perms[1]:
 #   mess.append(reference[i])
    
 # print mess
	  