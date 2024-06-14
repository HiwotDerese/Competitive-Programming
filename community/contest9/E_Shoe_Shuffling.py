t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int,input().split()))
	d = {}
	for i in a:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	# print(d)        

	v = list(d.values())
	if 1 in v:
		print(-1)
		
	else:
		temp = 0
		for k in d:
			# print(k, temp, 'kkk')
			print(temp+d[k],end=' ')
			
			for j in range(temp+1,temp+d[k]):
				print(j,end=' ')
				
			temp += d[k]
			
		print()
		