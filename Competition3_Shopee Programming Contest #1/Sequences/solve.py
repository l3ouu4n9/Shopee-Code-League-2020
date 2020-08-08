import itertools

items = []

N_M_K = input()
N, M, K = N_M_K.split()
N = int(N)
M = int(M)
K = int(K)

for i in range(N):
	A_B_C = input()
	A, B, C = A_B_C.split()
	A = int(A)
	B = int(B)
	C = int(C)

	for j in range(1, C + 1):
		items.append((A * ((j % K) * (j % K) % K) % K) + B)


# use product
ans = 0
for com in list(itertools.product(items, repeat=M)):
	if sum(com) % K == 0:
		ans += 1

print(ans % ((10 ** 9) + 7))