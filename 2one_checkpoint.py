#code for 1 checkpoint
#take start,checkpoint and goal 
x1,y1=map(float,input("Enter the starting state for Robot (x,y)->").split())
c1,c2=map(float,input("Enter the checkpoint (x,y)->").split())
x2,y2=map(float,input("Enter the Goal state of Robot (x,y)->").split())

print("The waypoints are:")

#waypoint between start and checkpoint
for i in range(1,5):
    t=i/5
    x = x1 + t * (c1-x1)
    y = y1 + t * (c2-y1)
    print(round(x,2),round(y,2))

#waypoint between checkpoint and goal
for i in range(1,5):
    t=i/5
    x = c1 + t * (x2-c1)
    y = c2 + t * (y2-c2)
    print(round(x,2),round(y,2))