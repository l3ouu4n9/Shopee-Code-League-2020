case = int(input())

for c in range(case):
	print('Case {}:'.format(c + 1))
	N_Q = input()
	N, Q = N_Q.split()
	N = int(N)
	Q = int(Q)

	dbs = []

	for i in range(N):
		dbs.append(input())

	for j in range(Q):
		ans = 0
		query = input()
		for db in dbs:
			if query in db:
				ans += 1
		print(ans)