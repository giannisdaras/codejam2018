def move_backwards(my_list):
	swap_index=len(my_list)-1
	if (len(my_list)==1):
		return [-1,-1]
	running_index=swap_index-1
	while (running_index>=0):
		if (my_list[running_index]=="C"):
			return [running_index,swap_index]
		swap_index=running_index
		running_index=running_index-1
	return [-1,-1]

T=int(input())
for mm in range(T):
	tmp=list(input().split(' '))
	D=int(tmp[0])
	tmp2=list(tmp[1:])
	seq=[]
	for i in tmp2[0]:
		seq.append(i)
	L=len(seq)
	flag_unsolved=False
	flag_end=False
	total_penalty=0
	while (flag_unsolved==False and flag_end==False):
		attack_power=1
		damage=0
		index=0
		flag_problem=False
		while (index<L and flag_problem==False):
			if (seq[index]=="S"):
				damage=damage+attack_power
			else:
				attack_power=2*attack_power
			if (damage>D):
				flag_problem=True
				res=move_backwards(seq[0:index+1])
				running_index=res[0]
				swap_index=res[1]
				if (running_index==-1):
					flag_unsolved=True
				else:
					seq[swap_index]="C"
					seq[running_index]="S"
					total_penalty+=1
			index=index+1
		if (flag_problem==False):
			flag_end=True
	# moving to next testcase
	if (flag_unsolved==True):
		print("Case #{}: IMPOSSIBLE".format(mm+1))
	else:
		print("Case #{}: {}".format(mm+1,total_penalty))







