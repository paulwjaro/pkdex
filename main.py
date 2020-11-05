from prettytable import PrettyTable

pokedex = PrettyTable()
pokedex.add_column("Pokemon", ["Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise",
                               "Bulbasuar", "Ivysaur", "Venasaur"])
pokedex.add_column("Type", ["Fire", "Fire", "Fire/Flying", "Water", "Water", "Water", "Grass/Poison", "Grass/Poison",
                            "Grass/Poison"])

pokedex.align = "l"
pokedex.align["Pokemon"] = "c"
pokedex.align["Type"] = "c"

print(pokedex)
