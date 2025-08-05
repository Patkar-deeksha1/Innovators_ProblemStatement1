# Waypoint Generator for Robot Path Planning

This project provides a complete solution for generating smooth intermediate waypoints for robot navigation using linear interpolation. It supports:

1) Direct path (0 checkpoints)

2) Path with 1 checkpoint

3) Path with 0 to 2 checkpoints

4) Web-based visualization using Flask + HTML

Separate Python files for 0, 1, and 2 checkpoint path generation are included to understand the logic step-by-step.
The app.py file combines all these into one complete and final web application.



# Project Structure

waypoint-generator/
│
├── 1no_checkpoint.py          # program for 0 checkpoints
├── 2one_checkpoint.py         # program for 1 checkpoint
├── 3two_checkpoint.py         # program supporting 0 to 2 checkpoints
├── 4app.py                    # Flask web app (accepts form input and plots waypoints)
├── templates/
│   └── index.html             # HTML frontend for the Flask app
└── README.md                  # This file




## Features and Functionality

### 1no_checkpoint.py

- Input: Start and Goal coordinates (x, y)
- Output: 4 intermediate waypoints generated using 2-point linear interpolation


### 2one_checkpoint.py

- Input: Start, Checkpoint, and Goal coordinates
- Output: 8 total waypoints (4 between Start → Checkpoint and 4 between Checkpoint → Goal)


### 3two_checkpoint.py

- Input: Start, up to 2 Checkpoints, and Goal
- Output: 4 waypoints between each pair of points (Start → CP1 → CP2 → Goal = 12 waypoints)


4. 4app.py 

- Input through HTML form:
  - Start point
  - Optional: Checkpoint 1 and Checkpoint 2
  - Goal point
    
- Output:
  - List of intermediate waypoints
  - A matplotlib-generated graph image showing:
    - Start (Green)
    - Goal (Red)
    - Checkpoints (Orange)
    - waypoints (blue)


### 5. index.html

- This is the frontend form used by app.py
- Allows user to input coordinates for Start, up to 2 Checkpoints, and Goal
- Displays:
  - Generated waypoints in a list
  - Graphical visualization (from graph.png)
    

## Technology Stack

- Python
- Flask (Web Framework)
- HTML (Frontend form)
- Matplotlib (Graph plotting)



## How It Works (Logic)

### Linear Interpolation Formula (2-point method):

x = x1 + t * (x2 - x1)
y = y1 + t * (y2 - y1)

- Where t = i/5 for i in 1 to 4
- Generates 4 smooth intermediate points between two given coordinates


## Sample Output

For Start: (0, 0), Goal: (10, 10)


Waypoint 1: (2.0, 2.0)
Waypoint 2: (4.0, 4.0)
Waypoint 3: (6.0, 6.0)
Waypoint 4: (8.0, 8.0)


## Future Enhancements

- Obstacle avoidance and re-routing
- Dynamic user-defined number of waypoints
- Real-time animation of robot path

This project is open source and free to use for educational and research purposes.
