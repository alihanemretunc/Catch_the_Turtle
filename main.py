import turtle
import random
import time

# Sets up the game window
game_board = turtle.Screen()
game_board.bgcolor("white")
game_board.title("Catch the Turtle")

# Initializes score
score = 0

# Creates a turtle for displaying the score
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 250)
score_turtle.color('dark green')
score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# Function to update the score display
def update_score():
    score_turtle.clear()
    #score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# Below function generates a random turtle
def generate_turtle():
    turtle_instance = turtle.Turtle()
    turtle_instance.shape("turtle")
    turtle_instance.color('green')
    turtle_instance.penup()
    turtle_instance.shapesize(1.5)

    # Generates random position for the turtle
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle_instance.teleport(x, y)

    # Delay before hiding the turtle
    time.sleep(1)
    turtle_instance.hideturtle()

    # Registers mouse click event handler
    turtle_instance.onclick(turtle_clicked)

    # Adds turtle to active turtles list
    active_turtles.append(turtle_instance)

    return turtle_instance

# Function to handle turtle click events
def turtle_clicked(x, y):
    global score
    for turtle_instance in active_turtles:
        if turtle_instance.distance(x, y) < 20:
            score += 1
            print('Turtle clicked! Score: ', score)
            update_score()
            break

# A list for storing active turtles
active_turtles = []

# Function that updates the score display


# Main game loop
while True:
    # Generates a new turtle
    new_turtle = generate_turtle()

    game_board.update()





