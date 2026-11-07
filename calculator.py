num1 = input("Введите число: ")
action = input("Введите действие +, -, * или /: ")
num2 = input("Введите число: ")

num1 = int(num1)
num2 = int(num2)

if action == "+":
    print(num1 + num2)
elif action == "-":
    print(num1 - num2)
elif action == "*":
    print(num1 * num2)
elif action == "/":
    print(num1 / num2)
else:
    print("Действие не поддерживается")
