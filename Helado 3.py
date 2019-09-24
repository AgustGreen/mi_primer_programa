print("elije la respuesta con si/no")

quiero_helado_input = input("quieres comer helado?: ")
if quiero_helado_input == "si":
    quiero_helado= True
elif quiero_helado_input == "no":
    quiero_helado =False
else:
    print("solo puedes decir si o no, por lo tanto tomare tu respuesta como un no")

dinero_input = input("tienes dinero?: ")
if dinero_input == "no":
    tia_input = input("esta tu tia para pagarte el helado?: ")
heladero_present_input = input("esta el heladero?: ")

quiero_helado = quiero_helado_input
dinero = dinero_input
heladero_present = heladero_present_input

if quiero_helado == "si" and (dinero or tia_input == "si") and heladero_present == "si":
    print("comete tu helado")
else:
    print("no te comes nada")

