# Pergunta 1:
# Dado o Array de inteiros abaixo, ordene-o de tal forma que os números “1” estejam à esquerda. 
# Os itens devem ser modificados no lugar, ou seja, você não ira trocar posições e sim colocar os números “1” no inicio do Array.
# [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]


my_array = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

def sort (array):
    a = array
    b = []
    c = []
    d = []
    for i in a:
        if i == 1:
            b.append(i)
        else:
            c.append(i)

    for i in b:
        d.append(i)
    for i in c:
        d.append(i)
        
    return d
print ("Array original: ", my_array)        
print ("Array modificado: ", sort(my_array))