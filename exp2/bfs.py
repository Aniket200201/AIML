from collections import deque
def BFS(a, b, target):
     
    # Map is used to store the states
    m = {}
    isSolvable = False
    path = []
     
    # Queue to maintain states
    q = deque()
     
    # Initialing with initial state
    q.append((0, 0))
 
    # Iterate till our queue is not empty
    while (len(q) > 0):
         
        # Take the current state
        u = q.popleft()
        # Continue if this state is already visited
        if ((u[0], u[1]) in m):
            continue
 
        if ((u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0)):
            continue
 
        path.append([u[0], u[1]])
 
        # Marking current state as visited
        m[(u[0], u[1])] = 1
 
        # If we reach solution state, put ans=1
        if (u[0] == target or u[1] == target):
            isSolvable = True
             
            if (u[0] == target):
                if (u[1] != 0):
                    path.append([u[0], 0])
            else:
                if (u[0] != 0):
                    path.append([0, u[1]])
 
            # Print the solution path
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",",path[i][1], ")")
            break
 
        q.append([u[0], b]) 
        q.append([a, u[1]]) 
 
        for ap in range(max(a, b) + 1):
 
            # Pour current amount of water from Jug2 to Jug1
            c = u[0] + ap
            d = u[1] - ap
 
            if (c == a or (d == 0 and d >= 0)):
                q.append([c, d])
 
            # Pour current amount of water from Jug 1 to Jug2
            c = u[0] - ap
            d = u[1] + ap
 
            # Here,we check if this state is possible or not
            if ((c == 0 and c >= 0) or d == b):
                q.append([c, d])
         
        # Empty Jug2
        q.append([a, 0])
         
        # Empty Jug1
        q.append([0, b])
 
    # No, solution exists if ans=0
    if (not isSolvable):
        print ("No solution")
 
l = list(map(int, input("Enter jug capacities ").split()))
jug1 = l[0]
jug2 = l[1]
target_cap = 2
print("Path for solution state is:")
BFS(jug1,jug2,target_cap)
