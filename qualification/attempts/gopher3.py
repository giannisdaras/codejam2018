from collections import defaultdict
import sys	

class Graph:
	def __init__(self):
		self.graph=defaultdict(list)
	def addEdge(self,i,j,k,l):
		self.graph[(i,j)]
		self.graph[(k,l)]
		self.graph[(i,j)].append((k,l))
		self.graph[(k,l)].append((i,j))
	def bfs(self,source):
		visited=defaultdict(lambda: False)
		for i in self.graph.keys():
			visited[i]=False
		queue=[]
		queue.append(source)
		visited[source]=True
		counter=0
		while queue:
			currentNode=queue.pop(0)
			for i in self.graph[currentNode]:
				if (visited[i]==False):
					queue.append(i)
					visited[i]=True
			counter+=1
		return counter
def return_neighbors(source):
	i=source[0]
	j=source[1]
	return [(i-1,j),(i-1,j-1),(i-1,j+1),(i,j+1),(i,j-1),(i+1,j),(i+1,j-1),(i+1,j+1)]
T=int(input())
for k in range(T):
	A=int(input())
	my_graph=Graph()
	grid = [[0 for i in range(1002)] for j in range(1002)]
	grid[0]=[-1 for i in range(1002)]
	grid[1001]=[-1 for i in range(1002)]
	flag=True;
	print("{} {}".format(500,500))
	sys.stdout.flush()
	counter=0
	while(flag):
		counter+=1
		current_cell=list(map(int,input().split(' ')))
		if (current_cell[0]==current_cell[1] and (current_cell[1]==-1 or current_cell[1]==0) ):
			flag=False
		else:
			grid[current_cell[0]][current_cell[1]]=1
			for m in return_neighbors(current_cell):
				x=m[0]
				y=m[1]
				if (grid[x][y]==1):
					my_graph.addEdge(current_cell[0],current_cell[1],x,y)
			minim=100000
			node=(500,500)
			for i in my_graph.graph.keys():
				res=my_graph.bfs(i)
				if (res<minim):
					minim=res
					node=i
			print("{} {}".format(node[0],node[1]))
			sys.stdout.flush()



