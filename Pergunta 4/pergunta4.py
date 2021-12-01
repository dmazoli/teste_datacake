# Dado o array [9, 2, 3, 1, 4] encontre todos os números que estão faltando para completar o 
# intervalo 0 a n, onde n é o maior número dentro do array. Adicione os números faltando dentro do array.

my_array = [9, 2, 3, 1, 4]

def fill(array):
    bigger = max(array)
    temp_array = []
    for i in range(bigger):
        if i not in array:
            temp_array.append(i)
    array.extend(temp_array)
    return array

print("Meu array: ", my_array)

complete_array = fill(my_array)

print("Array com números faltando: ", complete_array)

complete_array.sort()

print("Array em ordem: ", complete_array)