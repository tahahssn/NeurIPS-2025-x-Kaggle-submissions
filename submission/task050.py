def p(c):
 G=[*map(list,c)]
 for _ in[0,1]:
  for r in G:
   i=-1
   try:
    while 1:i=r.index(8,i+1);j=r.index(8,i+1);r[i+1:j]=[3]*(j-i-1)
   except:0
  G=[*map(list,zip(*G))]
 return G