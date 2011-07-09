# 0-1 knapsack problem dynamic program
# David Eppstein, ICS, UCI, 2/22/2002

# each item to be packed is represented as a set of triples (size,value,name)
def itemSize(item): return item[0]
def itemValue(item): return item[1]
def itemName(item): return item[2]

# example used in lecture
exampleItems = [(3,3,'A'),
		(4,1,'B'),
		(8,3,'C'),
		(10,4,'D'),
		(15,3,'E'),
		(20,6,'F')]

exampleSizeLimit = 32

# inefficient recursive algorithm
# returns optimal value for given
#
# note items[-1] is the last item, items[:-1] is all but the last item
#
def pack1(items,sizeLimit):
	if len(items) == 0:
		return 0
	elif itemSize(items[-1]) > sizeLimit:
		return pack(items[:-1],sizeLimit)
	else:
		return max(pack(items[:-1],sizeLimit),
			   pack(items[:-1],sizeLimit-itemSize(items[-1])) +
				itemValue(items[-1]))

# refactor so all params are integers
#
def pack2(items,sizeLimit):
	def recurse(nItems,lim):
		if nItems == 0:
			return 0
		elif itemSize(items[nItems-1]) > lim:
			return recurse(nItems-1,lim)
		else:
			return max(recurse(nItems-1,lim),
				   recurse(nItems-1,lim-itemSize(items[nItems-1])) +
					itemValue(items[nItems-1]))
	return recurse(len(items),sizeLimit)

# memoize
#
# Unlike previous class examples, I'm going to use a Python dictionary
# rather than a list of lists, because it's similarly efficient but can
# handle double indexing better.  Also that way I can use the has_key method
# instead of having to initialize each entry with a flag value.
#
# The difference in actual syntax is dictionary[item1,item2] instead of
# listoflists[item1][item2], and an empty dictionary is {} instead of [].
# The extra pair of parens in has_key is also important.
#
def pack3(items,sizeLimit):
	P = {}

	def recurse(nItems,lim):
		if not P.has_key((nItems,lim)):
			if nItems == 0:
				P[nItems,lim] = 0
			elif itemSize(items[nItems-1]) > lim:
				P[nItems,lim] = recurse(nItems-1,lim)
			else:
				P[nItems,lim] = max(recurse(nItems-1,lim),
				    recurse(nItems-1,lim-itemSize(items[nItems-1])) +
					itemValue(items[nItems-1]))
		return P[nItems,lim]

	return recurse(len(items),sizeLimit)

# iterate
# 
# At this step we have to think about how to order the nested loops over
# the two indices nItems and lim.  Each recursive call involves nItems-1,
# so the natural choice is to make the outer loop be over values of nItems.
# The ordering in the inner loop is not so important.
#
# The recursive function definition and has_key lines have been replaced
# by a nested pair of loops.  All recursive calls have been replaced
# by dictionary lookups.
#
def pack4(items,sizeLimit):
	P = {}
	for nItems in range(len(items)+1):
		for lim in range(sizeLimit+1):
			if nItems == 0:
				P[nItems,lim] = 0
			elif itemSize(items[nItems-1]) > lim:
				P[nItems,lim] = P[nItems-1,lim]
			else:
				P[nItems,lim] = max(P[nItems-1,lim],
				    P[nItems-1,lim-itemSize(items[nItems-1])] +
					itemValue(items[nItems-1]))
	return P[len(items),sizeLimit]
	
# backtrack through the matrix of solution values to find actual solution
#
# Like the LCS problem, and unlike the matrix chain problem, we only need
# to backtrack along a single path in the matrix, so we can do it with a
# while loop instead of a recursion.  We add each item to the end of a
# list L, then reverse L to match the input order -- it would work to add
# each item to the beginning of L but that's much less efficient in Python.
#
def pack5(items,sizeLimit):
	P = {}
	for nItems in range(len(items)+1):
		for lim in range(sizeLimit+1):
			if nItems == 0:
				P[nItems,lim] = 0
			elif itemSize(items[nItems-1]) > lim:
				P[nItems,lim] = P[nItems-1,lim]
			else:
				P[nItems,lim] = max(P[nItems-1,lim],
				    P[nItems-1,lim-itemSize(items[nItems-1])] +
					itemValue(items[nItems-1]))

	L = []
	nItems = len(items)
	lim = sizeLimit
	while nItems > 0:
		if P[nItems,lim] == P[nItems-1,lim]:
			nItems -= 1
		else:
			nItems -= 1
			L.append(itemName(items[nItems]))
			lim -= itemSize(items[nItems])

	L.reverse()
	return L

# run the example
# output = ['A', 'C', 'F']
print pack5(exampleItems,exampleSizeLimit)
