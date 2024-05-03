import random

choices = ["Камінь", "Ножиці", "Папір"]
victory_count = 0
defeat_count = 0
draw_count = 0

def game_menu():
    print("Виберіть Камінь, Ножиці або Папір: ")
    print("1 - Камінь")
    print("2 - Ножиці")
    print("3 - Папір")
    print("Q/q/Й/й - Вихід з гри")
    return input("Ваш вибір: ")


player_choice = ""

while player_choice not in ["Q", "q", "Й", "й"]:
    player_choice = game_menu()

    if player_choice in ["Q", "q", "Й", "й"]:
        print("Кінець гри")
        print(f"Кількість перемог: {victory_count}, кількість поразок: {defeat_count}, кількість нічія: {draw_count}")
        break

    if player_choice in ["1", "2", "3"]:
        player_choice = choices[int(player_choice) - 1]
        computer_choice = random.choice(choices)

        print(f"Ваш вибір: {player_choice}")
        print(f"Вибір комп'ютера: {computer_choice}")

        if player_choice == computer_choice:
            print("Нічия!")
            draw_count += 1
        elif (player_choice == "Камінь" and computer_choice == "Ножиці") or \
            (player_choice == "Ножиці" and computer_choice == "Папір") or \
            (player_choice == "Папір" and computer_choice == "Камінь"):
                print("Ви виграли!")
                victory_count += 1
        else:
            print("Ви програли!")
            defeat_count += 1
    else:
        print("Помилковий вибір. Спробуйте ще раз.")

    print(f"Кількість перемог: {victory_count}, кількість поразок: {defeat_count}, кількість нічія: {draw_count}")
