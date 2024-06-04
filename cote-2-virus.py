import sys
import copy

def InputData():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	A = list(map(int, readl().split()))
	B = list(map(int, readl().split()))

	return N, M, A, B

def Find(start) :
	"""Go daeri's"""
	# for i in range(M) :
	# 	if B[i] != A[start + i] : return 0
	"""koosy"""
	V = copy.deepcopy(B)
	csum = sum(A[start:start+M])
	diff = (vsum - csum)/M
	for a in A[start:start+M]:
		try:
			V.pop(V.index(a + diff))
		except:
			return 0
	return 1

def Solve():
	sol = 0
	for i in range(N - M + 1) :
		sol += Find(i)
	return sol

sol = 0

N, M, A, B = InputData()
vsum = sum(B)
sol = Solve()
print(sol)
