#Reeborg's World - Navigating the maze
#See the problem at: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#Rationale behind the first while loop: Our strategy is to find the closest place where there is a wall to the right, and then follow that wall as much as possible
#until we reach the goal. Hence, we first make a beeline towards the nearest wall.
#After that, we move until we're at the goal, or until we find a free right turn. At the right turn, we turn right. If there is no free right or there is a wall in front,
#we turn left.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not wall_on_right():
    if front_is_clear():
        move()
    if right_is_clear():
        turn_right()
        move()
        
while not at_goal():
    while front_is_clear():
        move()
        if at_goal():
            break
        if right_is_clear():
            turn_right()
    turn_left()