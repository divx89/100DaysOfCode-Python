#Jump Hurdles
#See https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#for problem. The menu at the top can let you choose the hurdle number, from 1 till 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_wall():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump_wall()
    else:
        move()