print("Ejemplo de funciones")
# declarando funciones
def hola():
    print("Alguien uso la funcion hola")

def chat(mensa):
    print(f"Chat {mensa}")

def elcontesta(mensa):
    print(f"Chat el {mensa}")

def escribenombre(ap,n):
    print(f"Tu nombre completo es: {n} {ap}")

def suma(a,b):
    s=a+b
    return s

def resta(a,b):
    s=a-b
    return s

def mult(a,b):
    s=a*b
    return s

def division(a,b):
    s=a/b
    return s


#llamadas a funciones
hola()
chat("que bonito estas")
elcontesta("gracias")
escribenombre("López", "Daniela") 

print("Operacion suma")
c1=int(input("Ingresa un número"))
c2=int(input("Ingresa un número"))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

print("Operacion resta")
c3=int(input("Ingresa un número"))
c4=int(input("Ingresa un número"))
dameresta=resta(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")

print("Operacion multiplica")
c5=int(input("Ingresa un número"))
c6=int(input("Ingresa un número"))
damemult=mult(c5,c6)
print(f"La multiplicaion  de {c5} * {c6} = {damemult}")

print("Operacion divide")
c7=int(input("Ingresa un número"))
c8=int(input("Ingresa un número"))
damedivision=division(c7,c8)
print(f"La division de {c7} / {c8} = {damedivision}")
