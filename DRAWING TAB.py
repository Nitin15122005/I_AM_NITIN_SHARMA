import turtle
from turtle import *

screen = Screen()
screenMinX = -screen.window_width() / 2
screenMinY = -screen.window_height() / 2
screenMaxX = screen.window_width() / 2
screenMaxY = screen.window_height() / 2

screen.setworldcoordinates(screenMinX, screenMinY, screenMaxX, screenMaxY)

brush_turtle = Turtle()
brush_turtle.goto(0, 0)
brush_turtle.speed(10)


# Set up event handler to have the brush_turtle draw a line
# to the point that the user clicks on
def on_screen_click(x, y):
    # print "%d, %d" % (x, y)
    if y < screenMaxY - 40:  # only draw if clicked below color squares
        brush_turtle.goto(x, y)


screen.onclick(on_screen_click)


class ColorPicker(Turtle):
    def __init__(self, color="red", num=0):
        Turtle.__init__(self)
        self.num = num
        self.color_name = color
        self.speed(0)
        self.shape("circle")
        self.color("black", color)
        self.penup()

        # hack to register click handler to instance method
        self.onclick(lambda x, y: self.handle_click(x, y))

    def draw(self):
        self.setx(screenMinX + 110 + self.num * 30)
        self.sety(screenMaxY - 20)

    def handle_click(self, x, y):
        if self.color_name == "#F9F9F9":
            brush_turtle.penup()
            brush_turtle.color("black")
        else:
            brush_turtle.pendown()
            brush_turtle.color(self.color_name)


# Suppress animations while interface is being drawn
screen.tracer(0)

ui_turtle = Turtle()
ui_turtle.ht()
ui_turtle.penup()
ui_turtle.goto(screenMinX, screenMaxY - 23)
ui_turtle.write("TurtleDraw!", align="left", font=("Courier", 10, "bold"))

# Create color choosing squares at the top of screen
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "#F9F9F9"]
color_pickers = [ColorPicker(color=c, num=i) for i, c in enumerate(colors)]
for picker in color_pickers:
    picker.draw()

# Resume animations now that main interface has been drawn
screen.tracer(1)
turtle.done()