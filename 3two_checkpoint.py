#code for 2 checkpoints
def generateWaypoints(start, goal, waypoints_to_find=4):
    x1,y1=start
    x2,y2=goal
    waypoints=[]

     #calculate 4 waypoints per segment
    for i in range(1,5):
        t=i/5
        x = x1 + t * (x2-x1)
        y = y1 + t * (y2-y1)
        waypoints.append((round(x,2),round(y,2)))
    return waypoints

def main():
    points=[]

    x,y=map(float,input("Enter the satrting point for Robot (x,y)->").split())
    points.append((x,y))

    n=int(input("Enter the number of checkpoints (0-2):"))
    for i in range(n):
        x,y=map(float,input(f"Enter checkpoint {i+1} (x,y): ").split())
        points.append((x,y))
    
    x,y=map(float,input("Enter the Goal point for Robot(x,y): ").split())
    points.append((x,y))

    print("\nThe Waypoints generated are:")
    for i in range(len(points)-1):
        start=points[i]
        goal=points[i+1]
        waypoints=generateWaypoints(start,goal)

        for coordinate in waypoints:
            print(coordinate)

main()