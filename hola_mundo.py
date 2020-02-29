# Pedimos información
name = input("Introduce tu nombre: ")
age = input("Introduce tu edad: ")
age = int(age)

# Saludamos al usuario
print("Mucho gusto,", name)
print("Tu edad es:", age)

# Imprimimos de acuerdo a la edad
if 18 <= age < 100:
    print("Eres un(a) ciudadano(a).")
elif age >= 100:
    print("DEAD.")
else:
    print("Eres un(a) menor.")
