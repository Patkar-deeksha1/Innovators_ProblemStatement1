from flask import Flask,request,render_template
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os 

app=Flask(__name__)

def generateWaypoints(start,goal,waypoints_to_find=4):
    x1,y1=start
    x2,y2=goal
    waypoints=[]

    if x2==x1:
        t=(y2-y1) / 5
        for i in range (1,5):
            y=round(y1+ i * t, 2)
            waypoints.append((x1,y))
    else:
        m=(y2-y1) / (x2-x1)
        t=(x2-x1) / 5
        for i in range (1,5):
            x=x1 + i * t
            y=y1 + m * (x-x1)
            waypoints.append((round(x,2),round(y,2)))
    return waypoints

@app.route('/', methods=['GET', 'POST'])
def index():
    start=goal=None
    checkpoints=[]
    waypoints=[]

    if request.method== 'POST':
        x1,y1=float(request.form['start_x']),float(request.form['start_y'])
        x2,y2=float(request.form['goal_x']),float(request.form['goal_y'])
        start=(x1,y1)
        goal=(x2,y2)

        if request.form['cp1_x'] and request.form['cp1_y']:
            checkpoints.append((float(request.form['cp1_x']),float(request.form['cp1_y'])))
        
        if request.form['cp2_x'] and request.form['cp2_y']:
            checkpoints.append((float(request.form['cp2_x']),float(request.form['cp2_y'])))

        pathpoints=[start]+ checkpoints+[goal]

        for i in range(len(pathpoints)-1):
            start=pathpoints[i]
            goal=pathpoints[i+1]
            wp=generateWaypoints(start,goal)
            waypoints.extend(wp)

            plt.figure(figsize=(8,6))
            if pathpoints:
                plt.scatter(*pathpoints[0],color='green',label='Start',s=100)
                plt.scatter(*pathpoints[-1],color='red',label='Goal',s=100)

            for cp in checkpoints:
                plt.scatter(*cp,color='orange',label='checkpoint',s=100)

            if waypoints:
                x_value,y_value=zip(*waypoints)
                plt.scatter(x_value,y_value,color='blue',label='waypoints')            

            plt.xlabel('X Axis')
            plt.ylabel('Y Axis')
            plt.title('Graph Plot') 
            plt.legend()
            plt.grid(True) 
            plt.savefig('static/graph.png')
            plt.close()    

    return render_template('index.html', waypoints=waypoints)

if __name__=='__main__':
    app.run(debug=True)