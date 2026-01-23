def p(g):
	B=[0]*10
	for(E,C)in enumerate(g):
		for(D,A)in enumerate(C):
			if A:B[A]=C.count(A)*sum(B[D]==A for B in g)
	return[[B.index(max(B))]*2]*2