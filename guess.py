secret = 7

guess = input("Угадай число от 1 до 10: ")
guess = int(guess)

if guess == secret:
    print("Ты угадал. Число:", guess)
else:
    print("Ты не угадал. Загаданное число было", secret)