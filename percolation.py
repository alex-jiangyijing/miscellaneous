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

import random

n=500
N=250000
parent=[0]
Number=[1]
state=[0]

for x in range(1,N):
	parent.append(x)
	Number.append(1)
	state.append(0)

parent.append(N)
parent.append(N+1)
Number.append(1)
Number.append(1)

for y in range(n):
	WQUPC(y,N)
for z in range(N-n+1,N):
	WQUPC(z,N+1)

ranlist=random.sample(range(N),N)

for index in range(N):
	state[ranlist[index]]=1
	divide=divmod(ranlist[index],n)

	if (divide[0]<n-1) and (divide[0]>0) and (divide[1]<n-1) and (divide[1]>0):
		if state[ranlist[index]-1]==1:
			WQUPC(ranlist[index],ranlist[index]-1)
		if state[ranlist[index]+1]==1:
			WQUPC(ranlist[index],ranlist[index]+1)
		if state[ranlist[index]-n]==1:
			WQUPC(ranlist[index],ranlist[index]-n)
		if state[ranlist[index]+n]==1:
			WQUPC(ranlist[index],ranlist[index]+n)
	elif divide==[0,0]:
		if state[ranlist[index]+1]==1:
			WQUPC(ranlist[index],ranlist[index]+1)
		if state[ranlist[index]+n]==1:
			WQUPC(ranlist[index],ranlist[index]+n)
	elif divide==[0,n-1]:
		if state[ranlist[index]-1]==1:
			WQUPC(ranlist[index],ranlist[index]-1)
		if state[ranlist[index]+n]==1:
			WQUPC(ranlist[index],ranlist[index]+n)
	elif divide==[n-1,0]:
		if state[ranlist[index]+1]==1:
			WQUPC(ranlist[index],ranlist[index]+1)
		elif state[ranlist[index]-n]==1:
			WQUPC(ranlist[index],ranlist[index]-n)
	elif divide==[n-1,n-1]:
		if state[ranlist[index]-1]==1:
			WQUPC(ranlist[index],ranlist[index]-1)
		if state[ranlist[index]-n]==1:
			WQUPC(ranlist[index],ranlist[index]-n)
	elif (divide[1]==0) and (divide[0]>0) and (divide[0]<n-1):
		if state[ranlist[index]+1]==1:
			WQUPC(ranlist[index],ranlist[index]+1)
		if state[ranlist[index]-n]==1:
			WQUPC(ranlist[index],ranlist[index]-n)
		if state[ranlist[index]+n]==1:
			WQUPC(ranlist[index],ranlist[index]+n)
	elif (divide[1]==n-1) and (divide[0]>0) and (divide[0]<n-1):
		if state[ranlist[index]-1]==1:
			WQUPC(ranlist[index],ranlist[index]-1)
		if state[ranlist[index]-n]==1:
			WQUPC(ranlist[index],ranlist[index]-n)
		if state[ranlist[index]+n]==1:
			WQUPC(ranlist[index],ranlist[index]+n)
	elif (divide[0]==0) and (divide[1]>0) and (divide[1]<n-1):
		if state[ranlist[index]+1]==1:
			WQUPC(ranlist[index],ranlist[index]+1)
		if state[ranlist[index]-1]==1:
			WQUPC(ranlist[index],ranlist[index]-1)
		if state[ranlist[index]+n]==1:
			WQUPC(ranlist[index],ranlist[index]+n)
	elif (divide[0]==n-1) and (divide[1]>0) and (divide[1]<n-1):
		if state[ranlist[index]+1]==1:
			WQUPC(ranlist[index],ranlist[index]+1)
		if state[ranlist[index]-1]==1:
			WQUPC(ranlist[index],ranlist[index]-1)
		if state[ranlist[index]-n]==1:
			WQUPC(ranlist[index],ranlist[index]-n)
	
	if QuickFind(N,N+1)==1:
		print((index+1)/N)
		break



