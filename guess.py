number_guess = 2

user_number = int(input("adivina un numero del 1 al 10 (tienes 3 intentos): "))

if number_guess == user_number:
    print("has ganado!")
elif number_guess != user_number:
    print("has perdido, reintenta")


user_number = int(input("adivina un numero del 1 al 10 (tienes 2 intentos): "))

if number_guess == user_number:
    print("has ganado!")
elif number_guess != user_number:
    print("has perdido, reintenta")


user_number = int(input("adivina un numero del 1 al 10 (tienes 1 intento): "))

if number_guess == user_number:
    print("has ganado!")
elif number_guess != user_number:
    print("has perdido, reintenta")




