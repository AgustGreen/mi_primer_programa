quiero_helado_input = input("¿quieres un helado? (si/no): ").upper()

if quiero_helado_input == "SI":
    quiero_helado = True
elif quiero_helado_input == "NO":
    quiero_helado = False
else:
    print("Solo puedes responder Si o No, por lo que haremos de cuenta que es un No")
    quiero_helado = False

tengo_dinero_input = input("¿tienes dinero para un helado? (si/no): ").upper()
senor_helado_input = input("¿esta el señor de los helados? (si/no): ").upper()
esta_tia_input = input("¿esta tu tia para pagarlo? (si/no): ").upper()

quiero_helado = quiero_helado_input == "SI"
tengo_dinero = tengo_dinero_input == "SI"
esta_tia = esta_tia_input == "SI"
puedo_comprar = tengo_dinero or esta_tia == "SI"
senor_helado = senor_helado_input == "SI"

if quiero_helado and puedo_comprar and senor_helado:
    print("comete el helado")
else:
    print("entonces no te lo comas")





