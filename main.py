#Flappyball game
import pgzrun
import random

WIDTH = 800
HEIGHT = 400
TITLE = "Flappyball"
GRAVITY = 2000

#Random ball colors
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

color = (r, g, b)

#Class for ball
class Ball():
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw_circle(self):
        pos = (self.x , self.y)
        screen.draw.filled_circle(pos, self.radius, color)

#Objects for Ball class
b1 = Ball(50, 50)

def draw():
    screen.clear()
    screen.fill("pink")
    b1.draw_circle()

def update(dt):
    #v = u + (a*t)
    #v = final velocity
    #u = initial velocity
    #a = acceleration
    #t = time taken
    uy = b1.vy
    b1.vy = b1.vy + (GRAVITY * dt)

    #Displacement of ball in y-axis
    #s = (u + v) / 2 * t
    b1.y += (uy + b1.vy) * 0.5 * dt

    if b1.y > HEIGHT:
        b1.y = HEIGHT - b1.radius
        b1.vy = -b1.vy * 0.9

    #Displacement of ball in x-axis
    b1.x += b1.vx * dt

    if b1.x > WIDTH - b1.radius or b1.x < b1.radius:
        b1.vx = -b1.vx

def on_key_down(key):
    if key == keys.UP:
        b1.vy = -500


pgzrun.go()