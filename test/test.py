""" 
temp = ["con cho", "cc", "dd"]


def is_Exist(arr: [], val):
    for i in range(0, len(arr)):
        if arr[i] == val:
            return True

    return False


print(is_Exist(temp, "cc"))
temp.append('kakka')
print(temp)

while (len(temp) != 0):
    print(temp[0])
    temp.remove(temp[0])


print(temp)

cost = [100_000]*400
cost[17] = 0
print(cost) """

""" g:graphs, open_set:[], close_set:[]
def BFS_algorithm(g, open_set, close_set):
    currentList <- close_set
    while currentList != NULL:
        curNode <- currentList[0]
        if curNode == ggGoal:
            #set color path
            return
    
        close_set.append(curNode)
        open_set.remove(curNode)
        neighbors = curNode.get_neighbors()
        while neighbors != NULL:
            if (neighbors[0] not in open_set) and (neighbors[0] not in close_set):
                open_set.append(neighbors[0])

            neighbors.remove(neighbors[0])
    
    BFS_algorithm(g, open_set, close_set)
 """

def is_Exist(arr: [], val):
    for i in range(0, len(arr)):
        if arr[i] == val:
            return True

    return False

l1 = []
l2 = ["a", "b", "c"]
l1 = l1 + l2
l3 = l2
a = l1[0]
if not is_Exist(l2, "d"):
    print("cc")
l2.remove(a)
print(l1)
print(l2)
print(l3)

def test(list_):
    if(len(list_) == 0):
        return

    while len(list_) != 0:
        if(list_[0] == "a"):
            return
        list_.remove(list_[0])
    
    test(list_)


test(l1)
print(l1)

""" a = l1[len(l1) - 1]

l1.remove(a)
print(a)
print(l1) """


l2.append(l1[len(l1) - 1])
l1.remove(l1[len(l1) - 1])

print(l1)
print(l2)
