import turtle

def draw_petal():
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(100, 60)  # Bán kính và góc của cánh hoa
    turtle.left(120)
    turtle.circle(100, 60)
    turtle.left(120)
    turtle.end_fill()

def draw_flower():
    turtle.speed(2)  # Tốc độ vẽ
    for _ in range(6):  # Số cánh hoa
        draw_petal()
        turtle.left(60)  # Xoay để vẽ cánh hoa tiếp theo

    # Vẽ nhụy hoa
    turtle.penup()
    turtle.goto(0, -20)  # Vị trí nhụy hoa
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(20)  # Nhụy hoa
    turtle.end_fill()

def draw_stem():
    turtle.penup()
    turtle.goto(0, -20)  # Vị trí bắt đầu thân hoa
    turtle.setheading(-90)  # Hướng xuống dưới
    turtle.pendown()
    turtle.color("green")
    turtle.pensize(5)  # Độ dày của thân hoa
    turtle.forward(150)  # Chiều dài của thân hoa

def main():
    turtle.title("Flower Drawing")
    turtle.setup(width=400, height=600)
    turtle.bgcolor("white")  # Màu nền
    draw_flower()
    draw_stem()
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
