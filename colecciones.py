
# Ejemplo de listas con Python
skills = [
    "Python", # 0
    "HTML",   # 1
    "CSS",    # 2
    "CMD"     # 3
]

# Accedemos a elementos de una lista con índices
print(skills)
print(skills[2])

# Ciclo for
cajas_petri = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
total = 0
for cp in cajas_petri:
    if cp == 1:
        total = total + 1

print("Total de pp. con bactería:", total)
