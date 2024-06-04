import sys
import queue

def input_data() :
	readl = sys.stdin.readline
	N = int(readl())#협찬 물품의 수
	D = list(map(int, readl().split()))#선호도 
	return N, D

# def Solve():
# 	"""dolbom's"""
# 	# sol = -30001#첫번째 방법의 최대 선호도
# 	# for i in range(0,N-2) :
# 	# 	t = sum(D[i:i+3])
# 	# 	if(t > sol) : sol = t
# 	# return sol
# 	"""timeout: 9~""" --> n^3
# 	# sol = -30001#첫번째 방법의 최대 선호도
# 	# for i in range(1, N+1):
# 	# 	for j in range(N-(i-1)):
# 	# 		t = sum(D[j:j+i])
# 	# 		if(t > sol) : sol = t
# 	# return sol
# 	"""timeout: 11~""" --> n^2 (n=10^5 정도면 n이나 nlogn 정도의 복잡도)
# 	sol = -30001#첫번째 방법의 최대 선호도
# 	for i in range(N-1):
# 		t = 0
# 		for j in range(i, N):
# 			t = t + D[j]
# 			if(t > sol): sol = t
# 	return sol

"""dfs:timeout:6,7; runtime error:8~"""
# sol = -30001 #첫번째 방법의 최대 선호도
# def dfs(st, ed):
# 	global sol
# 	if(ed - st < 1):
# 		return

# 	t = sum(D[st:ed])
# 	if(t > sol): sol = t
	
# 	dfs(st+1, ed)
# 	dfs(st, ed-1)

"""강의솔루션 듣고 구현"""
def Solve():
	sol = -30001#첫번째 방법의 최대 선호도
	for i in range(N-1):
		t = 0
		for j in range(i, N):
			t = t + D[j]
			if(t > sol): sol = t
			if (t < 0): break
			
	return sol

"""강의해답:fail:3,6"""
# def Solve():
# 	sol = -30001#첫번째 방법의 최대 선호도
# 	t = 0
# 	for i in range(N-1):
# 		if (t > 0): t = t + D[i]
# 		else:				t = D[i]
# 		if(t > sol): sol = t

# 	return sol

N, D = input_data()
sol = Solve()
# dfs(0, N)
print(sol)