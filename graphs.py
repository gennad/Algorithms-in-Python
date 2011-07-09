# Adjacency lists
a, b, c, d, e, f, g, h = range(8)
N = [
    [b, c, d, e, f], # a
    [c, e], # b
    [d], # c
    [e], # d
    [f], # e
    [c, g, h], # f
    [f, h], # g
    [f, g] # h
]

# Adjacency dicts with Edge Weights
a, b, c, d, e, f, g, h = range(8)
N = [
    {b:2, c:1, d:3, e:9, f:4}, # a
    {c:4, e:3}, # b
    {d:8}, # c
    {e:7}, # d
    {f:5}, # e
    {c:2, g:2, h:2}, # f
    {f:1, h:6}, # g
    {f:9, g:8} # h
]

# A Dict with Adjacency Sets
N = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}

# An Adjacency Matrix, Implemented with Nested Lists
a, b, c, d, e, f, g, h = range(8)
N = [[0,1,1,1,1,1,0,0],
[0,0,1,0,1,0,0,0],
[0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,1,0,0,0,1,1],
[0,0,0,0,0,1,0,1],
[0,0,0,0,0,1,1,0]]

# A Weight Matrix with Infinite Weight for Missing Edges
a, b, c, d, e, f, g, h = range(8)
_ = float('inf')
W = [[0,2,1,3,9,4,_,_],
[_,0,4,_,3,_,_,_],
[_,_,0,8,_,_,_,_],
[_,_,_,0,7,_,_,_],
[_,_,_,_,0,5,_,_],
[_,_,2,_,_,0,2,2],
[_,_,_,_,_,1,0,6],
[_,_,_,_,_,9,8,0]]

def recursive_dfs(graph, start, path=[]):
  """Recursive depth first search from start."""
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def iterative_dfs(graph, start, path=[]):
  """Iterative depth first search from start."""
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path

def iterative_bfs(graph, start, path=[]):
  """Iterative breadth first search from start."""
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  return path

"""
   +---- A
   |   /   \
   |  B--D--C
   |   \ | /
   +---- E
"""

graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print 'recursive dfs ', recursive_dfs(graph, 'A')
print 'iterative dfs ', iterative_dfs(graph, 'A')
print 'iterative bfs ', iterative_bfs(graph, 'A')
