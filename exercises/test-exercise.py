"""
Concatenar las siguientes listas
Restricción: Utilizar el método extend
"""

lista_a = [1, 2, 3]
lista_b = ["4", "5", "6"]
lista_c = ["siete", "ocho", "nueve"]

# COMPLETAR - INICIO
listas_concatenadas_01 = lista_a
listas_concatenadas_01 = lista_b
listas_concatenadas_01.extend(lista_c)
# COMPLETAR - FIN

print(listas_concatenadas_01)
assert listas_concatenadas_01 == [1, 2, 3, "4", "5", "6", "siete", "ocho", "nueve"]
