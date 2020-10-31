def solution(map):
  h = len(map)
  w = len(map[0])
  queue = [(0,0)] # (index, wall count)
  cnt=0 # count steps
  t = h*w-1
  visited = set()
  while len(queue) > 0:
    #print(queue)
    cnt+=1
    queue_tmp = set()
    for i in queue:
      #print(i)
      visited.add(i) # accept nodes with same index, but different wall count
      for nb in getNeighbors(i,w,h,map):
        if nb[0]==t: return cnt+1
        if nb not in visited: queue_tmp.add(nb)
      #print('queue_tmp', queue_tmp)
      #p = raw_input()
    queue = queue_tmp

  return cnt+1 # oops

def getNeighbors(x, w, h, map):
  r,c = getPos(x[0],w)
  nb = []
  # find all next posible squares
  for ofs in [(0,-1),(0,1),(-1,0),(1,0)]:
    r_n,c_n = (r+ofs[0], c+ofs[1])
    if r_n in range(0,h) and c_n in range(0,w) and not (x[1]==1 and map[r_n][c_n]):
      cnt = x[1]
      if map[r_n][c_n]: cnt+=1
      nb.append((r_n*w + c_n,cnt))
  return nb

def getPos(x,w):
  return x/w,x%w # row, column

