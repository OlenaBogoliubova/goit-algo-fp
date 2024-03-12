import turtle


def draw_pifagor_tree(branch_length, t, recursion_level):
    if recursion_level == 0:
        return
    else:
        t.forward(branch_length)
        t.right(45)
        draw_pifagor_tree(0.6 * branch_length, t, recursion_level - 1)
        t.left(90)
        draw_pifagor_tree(0.6 * branch_length, t, recursion_level - 1)
        t.right(45)
        t.backward(branch_length)


def main():
    # Запит користувача про рівень рекурсії
    recursion_level = int(
        input("Введіть рівень рекурсії для дерева Піфагора: "))

  # Налаштування екрану для відображення
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Створення черепашки
    t = turtle.Turtle()
    t.speed(2)  # Швидкість візуалізації

    # Початковий кут і місце для малювання
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    # Виклик функції для малювання дерева Піфагора
    draw_pifagor_tree(100, t, recursion_level)

    # Завершення програми при кліку мишею
    screen.exitonclick()


if __name__ == "__main__":
    main()
