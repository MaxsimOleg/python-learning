try:
    num1 = float(input("Введите число: "))
    action = input("Введите действие +, -, * или /: ")
    num2 = float(input("Введите число: "))
except:
    print("Нужно ввести число")
    exit()

if action == "+":
    print(num1 + num2)
elif action == "-":
    print(num1 - num2)
elif action == "*":
    print(num1 * num2)
try:
    if action == "/":
        print(num1 / num2)
except ZeroDivisionError:
    print ("На ноль делить нельзя")
    exit()