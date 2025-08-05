#code for 0 checkpoint
#take the input
x1,y1=map(float,input("Enter the starting point of Robot (x,y)->").split())
x2,y2=map(float,input("Enter the goal point of the Robot (x,y)->").split())

print("The waypoints for the Robot are:")

#4 waypoints so 1 to 5
for i in range(1,5):
    t=i/5

    #2 point formula
    x = x1 + t * (x2-x1)
    y = y1 + t * (y2-y1)

    #print rounded waypoints
    print(round(x,2),round(y,2))
