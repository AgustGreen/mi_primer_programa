initial_number = 10

print(initial_number)
if initial_number % 2 == 0:
    print("Este numero es par")
else:
    print("Este numero es impar")

while initial_number > 0:
    initial_number -= 1
    print(initial_number)
    if initial_number %2 == 0:
        print("Este numero es par")
    else:
        print("Este numero es impar")

print("He termiando")

