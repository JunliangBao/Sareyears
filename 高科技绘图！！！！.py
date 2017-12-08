import turtle
import time

t = turtle.Pen()

t.goto(0,0)
t.pencolor(input("颜色（英文）："))
t.pensize(5)
t.pendown()
t.speed(100)

#绘制正方形
#传递参数的绘制正方形程序
def square(side):
    for i in range(4):
        t.forward(side)
        t.left(90)

#旋转正方形
def rotated_squares(times):
    for i in range(times):
        square(100)
        square(130)
        square(160)
        t.left(360/times)
a = int(input("输入个数:"))        
rotated_squares(a)

time.sleep(2)