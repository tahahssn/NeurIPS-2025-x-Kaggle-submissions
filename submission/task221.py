R=range
def p(g):c=len([v for r in g for v in r if v]);L=9-c;m=[g[i]*min(max(0,c-I*L),L)+[0]*3*(L-max(0,c-I*L))for I in R(L)for i in R(3)];return m