def trouble_sort(L):
	done=False
	length=len(L)
	while (done==False):
		done=True
		for i in range(0,length-2):
			if (L[i]>L[i+2]):
				done=False
				l_i=L[i]
				L[i]=L[i+2]
				L[i+2]=l_i
	return L

T=int(input())
for i in range(T):
	list_length=int(input())
	my_inp=list(map(int,input().split(' ')))
	sorted_trouble=trouble_sort(my_inp)
	sorted_list=sorted(my_inp)
	flag=False
	index=0
	j=0
	while ( (not flag) and j<len(my_inp)):
		if (sorted_trouble[j]!=sorted_list[j]):
			index=j
			flag=True
		j+=1
	if (flag==False):
		print("Case #{}: OK".format(i+1))
	else:
		print("Case #{}: {}".format(i+1,index))
