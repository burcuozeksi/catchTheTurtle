import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("light yellow")
drawing_board.title("Catch the Turtle")
game_over = False
score = 0
FONT = ('Ariel', 20, 'normal')



#turtle list
turtle_list = []

#countdown turtle
count_down_turtle = turtle.Turtle()

#score turtle
score_turtle = turtle.Turtle()



# make turtle properties
x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]
grid_size = 13
def setup_score_turtle():

    score_turtle.hideturtle()
    score_turtle.color("dark red")
    score_turtle.penup()

    top_height = drawing_board.window_height() / 2
    y = top_height - top_height / 10
    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score:0", move=False, align="center", font= FONT)





#make turtle

def make_turtle(x, y):

    my_turtle = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score= {score}", move=False, align="center", font=FONT)

        #print(x, y)


    my_turtle.onclick(handle_click)
    my_turtle.penup()
    my_turtle.shape("turtle")
    my_turtle.shapesize(2, 2)
    my_turtle.color("green")
    my_turtle.goto(x * grid_size, y * grid_size)
    my_turtle.pendown()
    turtle_list.append(my_turtle)



def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)
def hide_turtles():
    for my_turtle in turtle_list:
        my_turtle.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        drawing_board.ontimer(show_turtles_randomly, 500) #recursive function

def countdown(time):
    global game_over

    top_height = drawing_board.window_height() / 2
    y = top_height - top_height / 10
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0, y - 30)
    count_down_turtle.clear()


    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        drawing_board.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)


def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()

    turtle.tracer(1)
    drawing_board.ontimer(lambda: countdown(10), 10)
start_game_up()
turtle.mainloop()
