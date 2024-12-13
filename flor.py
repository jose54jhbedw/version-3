import turtle

def draw_petal(t, radius):
    for _ in range(2):
        t.circle(radius, 60)  # Dibuja un arco de 60 grados
        t.left(120)           # Gira 120 grados para preparar el siguiente arco

def draw_flower():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Flor con Turtle")

    flower = turtle.Turtle()
    flower.speed(0)  # Velocidad minima
    flower.color("purple", "pink")

    flower.penup()
    flower.goto(0, -200)  # Ajusta la posición inicial
    flower.pendown()

    flower.begin_fill()
    for _ in range(12):  # Dibuja 78 pétalos
        draw_petal(flower, 100)
        flower.right(30)  # Gira para el siguiente pétalo
    flower.end_fill()

    # Dibuja el centro de la flor
    flower.penup()
    flower.goto(0, -65)
    flower.pendown()
    flower.color("pink")
    flower.begin_fill()
    flower.circle(30)
    flower.end_fill()

    flower.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_flower()
