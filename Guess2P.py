sel_number = input("Escribe un número (del 1 al 10); el segundo jugador deberá adivinarlo: ")
guess_number = input("Adivina el número (del 1 al 10): ")

while guess_number != sel_number:
    guess_number = input("Incorrecto, reintenta: ")

if guess_number == sel_number:
    print("¡Has acertado!")








