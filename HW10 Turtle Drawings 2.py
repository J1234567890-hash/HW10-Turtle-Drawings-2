import turtle
import random
from time import sleep
t = turtle.Turtle()
screen = turtle.Screen()

t.shape("turtle")
t.speed(0)
screen.bgcolor("black")

screen.setup(999, 999)

colors = ["red", "orange", "yellow", "green", "blue", "violet", ""]
allturtlecolors = ["black", "blue", "brown", "cyan", "gray", "green", "lightblue", "lightgreen",
    "lime", "magenta", "orange", "pink", "purple", "red", "violet", "white", "yellow",
    "aliceblue", "antiquewhite", "aquamarine", "azure", "beige", "bisque", "blanchedalmond",
    "blueviolet", "chartreuse", "chocolate", "coral", "cornflowerblue", "crimson", "darkblue",
    "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen",
    "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray",
    "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dodgerblue", "firebrick",
    "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "greenyellow",
    "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush",
    "lawngreen", "lemonchiffon", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightpink",
    "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightsteelblue", "lightyellow",
    "limegreen", "linen", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen",
    "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream",
    "mistyrose", "moccasin", "navajowhite", "oldlace", "olivedrab", "orangered", "orchid", "palegoldenrod",
    "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum",
    "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seashell",
    "sienna", "skyblue", "slateblue", "slategray", "snow", "springgreen", "steelblue", "tan", "teal", "thistle",
    "tomato", "transparent", "turquoise", "violet", "wheat", "whitesmoke", "yellowgreen"
    ]

# def hexagonSpiral(lines):
#     colorCount = 0
#     lineunits = 10
#     for i in range(lines):
#         for i in range(6):
#             if colorCount < 6 and colorCount > 0:
#                 colorCount = colorCount
#             else:
#                 colorCount = 0
#             t.color(colors[colorCount])
#             t.forward(lineunits)
#             t.left(59)
#             colorCount += 1
#         lineunits += 1        

# def hexagonSpiral2(lines):
#     colorCount = 0
#     lineunits = 10
#     for i in range(lines):
#         if colorCount < 6 and colorCount > 0:
#             colorCount = colorCount
#         else:
#             colorCount = 0
#         t.color(colors[colorCount])
#         t.forward(lineunits)
#         t.left(59)
#         colorCount += 1
#         lineunits += 1   
            
# def reset():
#     sleep(2)
#     screen.clear()
#     screen.bgcolor("black")
#     t.penup()
#     t.goto(0,0)
#     t.pendown()
#     t.setheading(0)

# lineCount = int(screen.textinput("Line Count", "How many lines do you want?"))
# hexagonSpiral2(lineCount)
# reset()
# lineCount = int(screen.textinput("Line Count 2", "How many lines do you want?"))
# hexagonSpiral(lineCount)
# reset()

# def randomSquares(squares, color):
#     length = random.randint(50, 200)
#     t.fillcolor(color)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(length)
#         t.left(90)
#     t.end_fill()

# squareCount = int(screen.textinput("Square Count", "How many squares do you want?"))
# for i in range(squareCount):
#     t.penup()
#     x = random.randint(-400,400)
#     y = random.randint(-400,400)
#     t.goto(x, y)
#     t.pendown()
#     # randomColor = random.randint(0, len(colors)-1)
#     # cloverColor = colors[randomColor]
#     squareColor = random.choice(allturtlecolors) # chooses a random color from the list
#     randomSquares(squareCount,squareColor)

# def spirograph(circles, radius, color1, color2):
#     for i in range(circleCount):
#         if i % 2 == 0:
#             t.color(color1)
#         else:
#             t.color(color2)
#         t.circle(radius)
#         t.left(12)

# reset()
# circleCount = int(screen.textinput("Circle Count", "How many circles do you want?"))
# circleRadii = int(screen.textinput("Circle Radii", "What should the radii of the circles be?"))
# Circlecolor1 = screen.textinput("Color 1", "What should the first color be?")
# Cirlcecolor2 = screen.textinput("Color 2", "What should the first color be?")
# spirograph(circleCount, circleRadii, Circlecolor1, Cirlcecolor2)

def smileyFaces(color):
    circlex = -300
    smilex = -330
    eye1x = -330
    eye2x = -260
    for i in range(3):
        t.penup()
        t.goto(circlex, 200)
        t.pendown()
        t.color("black", color)
        t.begin_fill()
        t.circle(100)
        t.end_fill()
        t.penup()
        t.goto(smilex,280)
        t.pendown()
        t.setheading(270)
        t.circle(35, 180)
        t.penup()
        t.goto(eye1x,330)
        t.pendown()
        t.dot(20)
        t.penup()
        t.goto(eye2x,330)
        t.pendown()
        t.dot(20)
        circlex += 300
        smilex += 300
        eye1x += 300
        eye2x += 300

smileyfaceColor = screen.textinput("Smiley Face Color", "What color should the smiley faces be?")
smileyFaces(smileyfaceColor)


screen.exitonclick()
