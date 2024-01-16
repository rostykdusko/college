# Основні типи даних
a = "змінна з текстом"
b = 1  # числова Змінна
c = ["a", 1, 1.25, "Слово"]  # List
d = {"a": "Слово", "b": 1}  # Dict
e = ("a",)  # Tuple
f = {"ss", }  # Set

# Виведення основних типів даних
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print("f:", f)

# Виведення вбудованих констант
print("та:", 3.14)
print("брехня:", False)

# Виведення результату роботи вбудованих функцій
print("abs(-12.5):", abs(-12.5))
print("abs(12.5):", abs(12.5))

# Цикли
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")

# Розгалуження
A = True
print("Значить А=True" if A else "Значить А=False")

# Конструкція try->except->finally
A = 0
try:
    print("Що буде якщо", 10/A, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")

# Контекст-менеджер with
with open("README.md", "r") as f:
    for line in f:
        print(line)

# Python lambdas
this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Дусько', 'Ростик'))
