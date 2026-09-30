import turtle
import random
import time

W, H = 800, 600
score = high_score = 0
delay = .1
running = True

screen = turtle.Screen()
screen.title("Mouse Hunt🐭")
screen.bgcolor("#8B5A2B")
screen.setup(W, H)
screen.tracer(0)

def make(shape, color, size):
    t = turtle.Turtle(shape)
    t.color(color)
    t.shapesize(size)
    t.penup()
    return t

# SNAKE
head = make("circle", "#1E8B3B", .9)
head.direction = "stop"

eye1 = make("circle", "white", .22)
eye2 = make("circle", "white", .22)
pupil1 = make("circle", "black", .1)
pupil2 = make("circle", "black", .1)

parts = []

def face():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "right":
        eye1.goto(x + 6, y + 6); eye2.goto(x + 6, y - 6)
        pupil1.goto(x + 8, y + 6); pupil2.goto(x + 8, y - 6)
    elif head.direction == "left":
        eye1.goto(x - 6, y + 6); eye2.goto(x - 6, y - 6)
        pupil1.goto(x - 8, y + 6); pupil2.goto(x - 8, y - 6)
    elif head.direction == "up":
        eye1.goto(x - 6, y + 6); eye2.goto(x + 6, y + 6)
        pupil1.goto(x - 6, y + 8); pupil2.goto(x + 6, y + 8)
    elif head.direction == "down":
        eye1.goto(x - 6, y - 6); eye2.goto(x + 6, y - 6)
        pupil1.goto(x - 6, y - 8); pupil2.goto(x + 6, y - 8)

# MOUSE
food = make("circle", "#777777", .8)
food.shapesize(.8, 1)

ear1 = make("circle", "pink", .45)
ear2 = make("circle", "pink", .45)
mouse_eye1 = make("circle", "black", .15)
mouse_eye2 = make("circle", "black", .15)
nose = make("circle", "pink", .22)

def new_mouse():
    x = random.randrange(-360, 361, 20)
    y = random.randrange(-260, 261, 20)

    food.goto(x, y)
    ear1.goto(x - 7, y + 9); ear2.goto(x + 7, y + 9)
    mouse_eye1.goto(x - 4, y + 3); mouse_eye2.goto(x + 4, y + 3)
    nose.goto(x, y - 5)

new_mouse()

# SCORE
pen = make("circle", "white", 1)
pen.hideturtle()
pen.goto(0, 260)

def score_display():
    pen.clear()
    pen.write(
        "Score: " + str(score) + "     High Score: " + str(high_score),
        align="center",
        font=("Arial", 18, "bold")
    )

score_display()

# CONTROLS
def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def left():
    if head.direction != "right":
        head.direction = "left"

def right():
    if head.direction != "left":
        head.direction = "right"

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# MOVEMENT
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# GAME OVER
over = make("circle", "red", 1)
over.hideturtle()

def game_over():
    over.clear()
    over.goto(0, 40)
    over.color("red")
    over.write("GAME OVER", align="center", font=("Arial", 34, "bold"))
    over.goto(0, -10)
    over.color("white")
    over.write("Final Score: " + str(score),
               align="center", font=("Arial", 20, "bold"))
    over.goto(0, -55)
    over.write("Press SPACE to restart",
               align="center", font=("Arial", 16))

# RESET
def reset():
    global score, running

    for part in parts:
        part.goto(1000, 1000)

    parts.clear()
    head.goto(0, 0)
    head.direction = "stop"
    score = 0
    running = True
    over.clear()
    new_mouse()
    score_display()

screen.onkeypress(reset, "space")

# GAME LOOP
while True:
    screen.update()

    if running:
        # Move the body from back to front
        for i in range(len(parts) - 1, 0, -1):
            parts[i].goto(parts[i - 1].xcor(), parts[i - 1].ycor())

        if len(parts) > 0:
            parts[0].goto(head.xcor(), head.ycor())

        move()
        face()

        # EAT MOUSE
        if head.distance(food) < 22:
            new_mouse()
            parts.append(make("circle", "#2E9B45", .8))

            score += 10
            high_score = max(high_score, score)
            score_display()

        # WALL COLLISION
        if abs(head.xcor()) > 380 or abs(head.ycor()) > 280:
            running = False
            game_over()

        # SELF COLLISION
        if running:
            for part in parts:
                if part.distance(head) < 15:
                    running = False
                    game_over()
                    break

    time.sleep(delay)
