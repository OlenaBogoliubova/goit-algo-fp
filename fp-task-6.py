def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорійність/вартість у спадаючому порядку
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    selected_items = {}
    remaining_budget = budget

    for item_name, item_data in sorted_items:
        if item_data["cost"] <= remaining_budget:
            selected_items[item_name] = item_data
            remaining_budget -= item_data["cost"]

    return selected_items


def dynamic_programming(items, budget):
    # Ініціалізуємо матрицю для збереження результатів
    dp_matrix = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    # Заповнюємо матрицю
    for i, (item_name, item_data) in enumerate(items.items(), start=1):
        for j in range(budget + 1):
            if item_data["cost"] <= j:
                dp_matrix[i][j] = max(
                    dp_matrix[i - 1][j], dp_matrix[i - 1][j - item_data["cost"]] + item_data["calories"])
            else:
                dp_matrix[i][j] = dp_matrix[i - 1][j]

    # Відновлюємо вибрані предмети
    selected_items = {}
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp_matrix[i][j] != dp_matrix[i - 1][j]:
            item_name = list(items.keys())[i - 1]
            selected_items[item_name] = items[item_name]
            j -= items[item_name]["cost"]
        i -= 1

    return selected_items


# Задані дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 75

# Застосовуємо обидва підходи
greedy_result = greedy_algorithm(items, budget)
dynamic_result = dynamic_programming(items, budget)

# Виводимо результати
print("Жадібний алгоритм:")
for item, data in greedy_result.items():
    print(f"{item}: Вартість - {data['cost']}, Калорії - {data['calories']}")

print("\nАлгоритм динамічного програмування:")
for item, data in dynamic_result.items():
    print(f"{item}: Вартість - {data['cost']}, Калорії - {data['calories']}")
