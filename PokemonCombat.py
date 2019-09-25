sel_pokemon = input("contra que pokemon quieres combatir?: (Squirtle / Bulbasaur / Charmander): ")

pikachu_hp = 100
enemy_hp = 0
enemy_atk = 0

if sel_pokemon == "Squirtle":
    enemy_hp = 90
    pokemon_name = "Squirtle"
    enemy_atk = 8
elif sel_pokemon == "Bulbasaur":
    enemy_hp = 100
    pokemon_name = "Bulbasaur"
    enemy_atk = 10
elif sel_pokemon == "Charmander":
    enemy_hp = 80
    pokemon_name = "Charmander"
    enemy_atk = 7

while pikachu_hp > 0 and enemy_hp > 0:
    sel_attack = input("Que ataque quieres usar? (Chispazo -10 / Bola voltio -12): ")
    if sel_attack == "Chispazo":
        print("Has utilizado Chispazo")
        enemy_hp -= 10
    elif sel_attack == "Bola voltio":
        print("Has utilizado Bola voltio")
        enemy_hp -= 12
    else:
        print("El ataque no es valido")
        enemy_hp -= 0

    print("La vida del {} es de {}".format(pokemon_name, enemy_hp))
    print(("{} te ha hecho {} de daño").format(pokemon_name, enemy_atk))
    pikachu_hp -= enemy_atk
    print("La vida de tu Pikachu es de {}".format(pikachu_hp))

if enemy_hp <= 0:
    print("Has ganado")

elif pikachu_hp <= 0:
    print("Has perdido")

print("El combate ha terminado")

