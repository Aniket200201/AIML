def match(p,x,y):
    global c1
    global c2
    if(p[0]==0 and p[1]==0):
        if(x==c1 and y==0):
            return True
        else:
            return False
    elif(p[0]!=0 and p[1]==c2):
        if(x==p[0] and y==0):
            return True
        else:
            return False
    elif(p[0]!=0 and p[1]>=0):
        temp=min(c2-p[1],p[0])
        right=p[1]+temp
        left=p[0]-temp
        # print(x,y)
        if(right==y and left==x):
            return True
        return False
    elif(p[0]==0 and p[1]>=0):
        if(x==c1 and y==p[1]):
            return True
        return False
    return False

def dfs(p):
    if(p[0]==2):
        return
    for i in range(0,5):
        for j in range(0,4):
            if(match(p,i,j)):
                p[0],p[1]=i,j
                print(i,j)
                dfs(p)
            else:
                continue
    return 1

a,b=0,0
c1=int(input('Enter the capacity of 1st jug :'))
c2=int(input('Enter the capacity of 2nd jug :'))
initial_point=[0,0]
print(*initial_point)
dfs(initial_point)
