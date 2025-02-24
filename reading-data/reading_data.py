people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10",
    "Dante 1"
]

# Inicializando valores para encontrar o mais jovem
youngest_age = float('inf')  # Definimos um valor inicial muito alto
youngest_person = ""

# Percorrer a lista para encontrar a pessoa mais jovem
for person in people:
    name, age = person.rsplit(" ", 1)  # Divide a string no último espaço
    age = int(age)  # Converte a idade para número inteiro

    if age < youngest_age:
        youngest_age = age
        youngest_person = name

# Exibir os resultados
print(f"A pessoa mais jovem é {youngest_person} com {youngest_age} anos.")


input("\nPressione Enter para sair...")