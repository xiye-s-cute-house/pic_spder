import time
import turtle


def drawGap():  # 用于绘制笔画,抬起笔，向前走五各单位长度
    turtle.penup()
    turtle.fd(5)


def drawLine(draw):  # 根据现在笔的状态进行控制笔的转向和走的长度
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)  # 右转90度


def drawDigit(d):  # 画出数字
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)  # g
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)  # c
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)  # d
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)  # e
    turtle.left(90)  # 经历一次右转后，调整左转，方向竖直向上
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):  # 格式化时间
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('时', font=('Arial', 18, 'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('分', font=('Arial', 18, 'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('秒', font=('Arial', 18, 'normal'))
            turtle.pencolor('yellow')
        else:
            drawDigit(eval(i))


def init():  # 初始化画布和笔
    turtle.setup(2000, 1100, 0, 0)  # 设置画布大小 200 200 为屏幕位置
    turtle.speed(10)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.fd(-350)
    turtle.pensize(5)


def main():
    # turtle.bgpic("E:\\pictures\\acg\\ec43126fgy1h0wydlh9j0j22xk1ub7wk.jpg")
    while True:
        turtle.clear()
        init()
        time_string = time.strftime("%H-%M=%S+", time.localtime())
        turtle.getscreen().tracer(30, 0)
        drawDate(time_string)  # 格式化时间 2017-05=02+ 控制输入年日月
        time.sleep(1)
        turtle.hideturtle()


main()
