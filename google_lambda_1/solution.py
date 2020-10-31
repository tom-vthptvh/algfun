def solution(x,y):
  if x==y: return 0
  queue = [x] # next posible squares
  visited = [] # keep track of visited squares
  cnt=0 # count steps
  while len(queue)>0:
    cnt=cnt+1
    queue_n = []
    #print('*queue:', queue)
    for i in queue:
      #print('p', i)
      visited.append(i)
      nb = getIndexNeighbors(i)
      #print('nb', nb)
      if y in nb: return cnt
      queue_n.extend([j for j in nb if j not in visited])
      #print('visited:', visited)
      #raw_input("Press Enter to continue...")
    queue = set(queue_n)
  return cnt

def getIndexNeighbors(x):
  r,c = getPos(x)
  nb = []
  # find all next posible squares
  for ofs in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
    r_n,c_n = (r+ofs[0], c+ofs[1])
    if r_n in range(0,8) and c_n in range(0,8):
      nb.append(r_n*8 + c_n)
  return nb

def getPos(x):
  return x / 8,x % 8 # row, column

for i in range(0,64):
  for j in range(i+1,64):
    print(i,j,solution(i,j))