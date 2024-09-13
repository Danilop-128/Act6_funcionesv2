print("Funciones version 2")
print("Daniela López")
# zona de listas, tuplas, conjuntos/sets y diccionarios
celulares=["Samsung a52","Iphone 11", "Chafa"]
flores=("Tulipan","Rosa", "Margarita")
prendas={"Sudadera","Pantalon", "Blusa"}
playasMundo={
    "Mexico:": "Playa del Carmen",
    "Grecia:": "Playa de Sarakiniko",
    "Filipinas:": "El Nido"
}

# zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)

def vertupla(flor):
    for unaflor in flor:
        print(unaflor)

def verconjunto(ropa):
    for unaprenda in ropa:
        print(unaprenda)

def verdiccionario(playas):
    for unaplaya, pla in playas.items():
        print(unaplaya, pla)

# Llamadas a funciones
print("Imprime celulares")
verlista(celulares)

print("Imprime flores")
vertupla(flores)

print("Imprime prendas")
verconjunto(prendas)

print("Imprime playas")
verdiccionario(playasMundo)