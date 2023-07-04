# Pattern given as integer 2d matrix
allPattern =[[1, 6, 4], [2, 4], [1], [4, 6, 1], [5, 3], [6, 2], [6, 4, 1], [4, 3, 6], [1, 2], [5], [5, 6, 2],
             [1, 3, 6], [4, 2], [4, 5], [6, 5, 1], [2, 1], [1, 2, 3], [3], [6], [2, 3], [1, 3, 6], [2, 1, 4],
             [2], [3, 2, 1], [1, 2], [1], [6, 5], [5, 1, 3], [3, 6], [3, 6, 4], [2, 4, 3], [6], [3], [1], [3],
             [2], [1, 2], [3, 5, 1], [2, 5, 1], [2], [5, 4], [2, 6, 5], [1], [1, 2, 6], [6, 2], [4], [2, 6],
             [6, 3, 2], [2, 6], [3]]


level = 3

# It includes all values of pattern
elements = []
for i in allPattern:
    for j in i :
        if not j in elements:
            elements.append(j)
elements.sort()


# It calculates how many node will be in the tree
level -= 1
numElements = len(elements)+1
numberOfNodes = (1 - (numElements-1)**(level + 1)) / (1 - (numElements-1))



# It is our Tree class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    index = None
    def add_child(self, child_node):
        self.children.append(child_node)

# All nodes has an index value
my_index = 0

# Creating a root of tree
root = TreeNode(-1)

root.index = my_index
my_index += 1
queue = list()

queue.append(root)



# It creates Tree
for i in range(int(numberOfNodes)):
    node = queue.pop(0)
    for i in elements:

        newNode= TreeNode(i)
        newNode.index= my_index
        my_index += 1

        node.add_child(newNode)
        queue.append(newNode)



#print(root.children[0].children[0].children[0].index)

node = root
childList = list()
for j in node.children:
    childList.append(j)


# It holds nodes as array
NodesToArray = list()
NodesToArray.append(root)

for i in range(int(numberOfNodes)):
    while childList:
        node = childList.pop(0)
        for j in node.children:
            childList.append(j)
        NodesToArray.append(node)

"""
Tree: Value of a root is 0 and every node has 6 child
Every node has an index that increases linearly.
(root.children[0].children[0].index= 7, root.children[0].children[0].children[0].index = 43 ) 
Height of a tree is 3 
"""

keys = list()

for i in range(len(NodesToArray)):
    temp = list()
    indexHolder = i

    while indexHolder>0:
        temp.append(NodesToArray[indexHolder].value)
        indexHolder = (indexHolder-1) // len(elements)
    temp.reverse()
    keys.append(temp)




"""
Tree stored as an array (NodesToArray)
keys list holds nodes and their parents values as a list
"""

# This step counts patterns and increase corresponding value in tree (values)
values = list()
for i in range(len(keys)):
    values.append(0)

for pattern in allPattern:
    node = root
    for step in pattern:
        for i in node.children:
            if i.value == step:
                val = values[i.index]
                val+=1
                values[i.index] = val
                #print(step, ":" , str(i.index) ,end = "  " )
                node = i
    #print()



patternDict = {tuple(key): value for key, value in zip(keys, values)}
print(patternDict)

