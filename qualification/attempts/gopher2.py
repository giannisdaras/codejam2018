import sys	
T=int(input())



for k in range(T):
	A=int(input())
	grid = [[0 for i in range(1002)] for j in range(1002)]
	grid[0]=[-1 for i in range(1002)]
	grid[1001]=[-1 for i in range(1002)]
	flag=True;
	print("{} {}".format(500,500))
	sys.stdout.flush()
	while(flag):
		current_cell=list(map(int,input().split(' ')))
		if (current_cell[0]==current_cell[1] and (current_cell[1]==-1 or current_cell[1]==0) ):
			flag=False
		else:
			grid[current_cell[0]][current_cell[1]]=1
			minim=8
			index_k=500
			index_l=500
			for k in range(450,550):
				for l in range(450,550):
					if (grid[k][l]==0):
						current=0
						if (grid[k-1][l]==0):
							current+=1
						if (grid[k-1][l-1]==0):
							current+=1
						if (grid[k-1][l+1]==0):
							current+=1
						if (grid[k][l-1]==0):
							current+=1
						if (grid[k][l+1]==0):
							current+=1
						if (grid[k+1][l]==0):
							current+=1
						if (grid[k+1][l-1]==0):
							current+=1
						if (grid[k+1][l+1]==0):
							current+=1
						if (current<minim):
							minim=current
							index_k=k
							index_l=l
			print("{} {}".format(index_k,index_l))
			sys.stdout.flush()




