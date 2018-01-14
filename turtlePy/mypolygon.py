import turtle
import math

bob = turtle.Turtle()
bob.speed(10)

for i in range(15000000):
    i += 10


def rhombus(t, color, ang, length):
    '''
    该函数用来画一个菱形
    ang参数代表画完一个菱形后转义的角度
    '''
    t.color(color, color) # 设置钢笔和填充颜色
    t.begin_fill() # 开始填充
    t.forward(length) # 正向移动
    t.right(45) # 向右转45°
    t.forward(length)
    t.right(135)
    t.forward(length)
    t.right(45)
    t.forward(length)
    t.right(ang) # 画完一个菱形后偏移一个角度
    t.end_fill() # 结束填充

for i in range(9):
    for p in range(5):
        if p == 1:
            rhombus(bob, 'red', 150, 180)

        if p == 2:
            rhombus(bob, 'blue', 150, 200)

        if p == 3:
            rhombus(bob, 'green', 150, 220)

        if p == 4:
            rhombus(bob, 'yellow', 150, 240)

turtle.mainloop()