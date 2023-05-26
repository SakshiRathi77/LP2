def create_tree():
    n=int(input("enter the no. of nodes you want to enter :"))
    d={}
    for i in range(n):
        print("Eneter the no. of node linked with ",i+1,": ")
        k=int(input())
        list_k=[]
        for j in range(k):
            print("enter the node linked with ", i+1,": ")
            ele=int(input())
            list_k.append(ele)
        d[i+1]=list_k
    print(d)
    return d


def dfs(d,start,visited=None):
    if visited==None:
        visited=set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in d[start]:      
        if neighbor not in visited:
            dfs(d,neighbor,visited)

def bfs(d, start):
    visited=set()
    queue=[start]
    visited.add(start)

    while(queue!=[]):
        pop_ele=queue.pop()
        print(pop_ele,end=" ")

        for i in d[pop_ele]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

d=create_tree()
dfs(d,1)
print()
bfs(d,1)

# 5
# 2
# 2
# 3
# 3
# 1
# 4
# 5
# 1
# 1
# 1
# 2
# 1
# 2


