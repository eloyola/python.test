peliculas = ["Batman", "Joker"]


numeros = [1, 2, 5, 3, 4]
# order
print(numeros)
numeros.sort()
print(numeros)

# insert
peliculas.append("The lord of the rings")
peliculas.insert(1, "Spiderman")
print(peliculas)

# delete
# peliculas.pop(1)
peliculas.remove("Spiderman")
print(peliculas)
#reverse
peliculas.reverse()
print(peliculas)
#search inside a list
print('Dracula' in peliculas)
#count
print(len(peliculas))
#how many time a value appears in a list
print(peliculas.count("Joker"))
#get index
print(peliculas.index("Joker"))
#join list
peliculas.extend(numeros)
print(peliculas)