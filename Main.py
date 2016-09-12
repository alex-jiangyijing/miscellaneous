def FindRoot(x):
	while parent[x]!=x:
		parent[x]=parent[parent[x]]
		x=parent[x]
	return x

def WQUPC(x,y):
	rootx=FindRoot(x)
	rooty=FindRoot(y)
	if Number[rootx]<Number[rooty]:
		parent[rootx]=rooty
		Number[rooty]=Number[rooty]+Number[rootx]
	elif Number[rootx]>=Number[rooty]:
		parent[rooty]=rootx
		Number[rootx]=Number[rootx]+Number[rooty]
	return

def QuickFind(x,y):
	if FindRoot(x)==FindRoot(y):
	   	Connect=1
	else:
		Connect=0
	return Connect

parent=[0,1,2,3,4,5,6,7,8,9]
Number=[1,1,1,1,1,1,1,1,1,1]
WQUPC(1,2)
WQUPC(4,5)
WQUPC(2,4)
WQUPC(6,5)
WQUPC(1,8)
print(parent[5])
print(parent[6])
print(Number[1])
print(QuickFind(1,7))
print(QuickFind(5,6))