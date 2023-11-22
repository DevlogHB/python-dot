import colorgram;
import turtle as t;
import random;

# 이미지 색상 추출
rgb_colors = [];
colors = colorgram.extract("image_color.jpg", 15);

for color in colors:
    r= color.rgb.r
    g= color.rgb.g
    b= color.rgb.b
    rgb_colors.append((r,g,b));

t.speed("fastest");
t.penup();
t.hideturtle();

t.colormode(255);

t.setheading(225);
t.forward(250);
t.setheading(0);

number_of_dots = 100
for num in range(1, number_of_dots + 1):
    t.dot(20, random.choice(rgb_colors));
    t.forward(50)

    if num % 10 == 0:
        t.setheading(90);
        t.forward(50);
        t.setheading(180);
        t.forward(500);
        t.setheading(0);

screen = t.Screen();
screen.exitonclick();