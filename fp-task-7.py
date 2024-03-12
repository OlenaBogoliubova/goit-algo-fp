import random
import matplotlib.pyplot as plt


def all_combinations(num_simulations):
    results = {}

    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2

        if total in results:
            results[total] += 1
        else:
            results[total] = 1

    probabilities = {key: (value / num_simulations) *
                     100 for key, value in results.items()}

    return probabilities


def display_table(probabilities):
    print("Таблиця сум та їх імовірностей:")
    print("Сума та Ймовірність (%)")
    for total, probability in sorted(probabilities.items()):
        print(f"{total}\t{probability:.2f}%")


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color='blue')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.xticks(sums)
    plt.show()


def main():
    num_simulations = int(input("Введіть кількість симуляцій: "))

    probabilities = all_combinations(num_simulations)

    display_table(probabilities)
    plot_probabilities(probabilities)


if __name__ == "__main__":
    main()
