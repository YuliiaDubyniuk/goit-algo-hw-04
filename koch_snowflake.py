import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    """Use turtle to draw Koch snowflake"""
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    window.mainloop()


def main():
    user_input = input("Please provide recursion depth: ")
    while not user_input.isdigit():
        user_input = input("Please enter a number from 1 to 10: ")

    draw_koch_snowflake(int(user_input))


if __name__ == "__main__":
    main()
