import sys

T=int(input())
for i in range(T):
	A=int(input())
	grid = [[0 for i in range(1002)] for j in range(1002)]
	grid[0]=[-1 for i in range(1002)]
	grid[1001]=[-1 for i in range(1002)]
	flag=True;
	sys.stdout.flush()
	print("{} {}".format(500,500))
	sys.stdout.flush()
	last_cell=[500,500]
	def find_common_neighbors(current_cell,last_cell,grid):
		neighbors_current=[]
		neighbors_last=[]
		k=current_cell[0]
		l=current_cell[1]
		n=last_cell[0]
		m=last_cell[1]
		if (grid[k-1][l]==0):
			neighbors_current.append([k-1,l])
		if (grid[k-1][l-1]==0):
			neighbors_current.append([k-1,l-1])
		if (grid[k-1][l+1]==0):
			neighbors_current.append([k-1,l+1])
		if (grid[k][l-1]==0):
			neighbors_current.append([k,l-1])
		if (grid[k][l+1]==0):
			neighbors_current.append([k,l+1])
		if (grid[k+1][l]==0):
			neighbors_current.append([k+1,l])
		if (grid[k+1][l-1]==0):
			neighbors_current.append([k+1,l-1])
		if (grid[k+1][l+1]==0):
			neighbors_current.append([k+1,l+1])
		if (grid[n-1][m]==0):
			neighbors_last.append([n-1,m])
		if (grid[n-1][m-1]==0):
			neighbors_last.append([n-1,m-1])
		if (grid[n-1][m+1]==0):
			neighbors_last.append([n-1,m+1])
		if (grid[n][m-1]==0):
			neighbors_last.append([n,m-1])
		if (grid[n][m+1]==0):
			neighbors_last.append([n,m+1])
		if (grid[n+1][m]==0):
			neighbors_last.append([n+1,m])
		if (grid[n+1][m-1]==0):
			neighbors_last.append([n+1,m-1])
		if (grid[n+1][m+1]==0):
			neighbors_last.append([n+1,m+1])
		for i in neighbors_current:
			for j in neighbors_last:
				if (i==j):
					return i
		return [-1,-1]
	while(flag):
		current_cell=list(map(int,input().split(' ')))
		if (current_cell[0]==current_cell[1] and (current_cell[1]==-1 or current_cell[1]==0) ):
			flag=False
		else:
			grid[current_cell[0]][current_cell[1]]=-1
			proposed_cell=find_common_neighbors(current_cell,last_cell,grid)
			if (proposed_cell[0]==-1):
				proposed_cell[0]=500
				proposed_cell[1]=500
			print("{} {}".format(proposed_cell[0],proposed_cell[1]))
			sys.stdout.flush()
			last_cell[0]=current_cell[0]
			last_cell[1]=current_cell[1]



