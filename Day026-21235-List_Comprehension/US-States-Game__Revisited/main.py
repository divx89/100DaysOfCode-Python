import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the file and get data
data = pandas.read_csv("./50_states.csv")
# Extract the names and make a list of those
state_names = data.state.to_list()
# We need the question/answer session going until 50 states are done
answer_list = []

while len(answer_list) < len(state_names):
    # Get an input
    answer = screen.textinput(title=f"Guess the State {len(answer_list)}/{len(state_names)}",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        break

    if answer in state_names and answer not in answer_list:
        answer_list.append(answer)

        state_data = data[data.state == answer]
        position = (int(state_data.x), int(state_data.y))

        state_text = turtle.Turtle()
        state_text.hideturtle()
        state_text.penup()
        state_text.goto(position)
        state_text.penup()
        state_text.write(arg=answer, align="center", font=("Courier", 8, "normal"))

# Replaced previous lines with list comprehension
missing_states = [state for state in state_names if state not in answer_list]
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")


screen.exitonclick()
