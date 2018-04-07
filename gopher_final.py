import sys

T=int(input())
for ml in range(T):
	A=int(input())
	grid = [[0 for i in range(1002)] for j in range(1002)]
	grid[0]=[-1 for i in range(1002)]
	grid[1001]=[-1 for i in range(1002)]
	current_x=500
	current_y=500
	flag_move_next_testcase=False
	while(not flag_move_next_testcase):
		flag_move_cell=False
		while (not flag_move_cell):
			print("{} {}".format(current_x,current_y))
			sys.stdout.flush()
			actual=list(map(int,input().split(' ')))
			actual_x=actual[0]
			actual_y=actual[1]
			if (actual_x==0 and actual_y==0):
				flag_move_next_testcase=True
				flag_move_cell=True
			elif (actual_x==-1 and actual_y==-1):
				sys.exit()
			else:
				grid[actual_x][actual_y]=1
				flag_move_cell=True
				for i in range(current_x-1,current_x+2):
					for j in range(current_y-1,current_y+2):
						if (grid[i][j]!=1):
							flag_move_cell=False
		current_y=current_y+3







