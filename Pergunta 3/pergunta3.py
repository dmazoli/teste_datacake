# Dado o array de números inteiros [1, 15, 2, 7, 2, 5, 7, 1, 4] crie uma função que recebe um 
# argumento X e retorne true ou false caso haja no array uma combinação de soma entre dois 
# números que resulte no input X. Exemplo: Se X=2, a função deve retornar true pois existem dois 
# números 1 dentro do array 1+1 = 2. Caso X=1231 a função deve retornar false pois não existe 
# uma combina de dois números capazes de somar 1231.

def test_sum (test_array, sum):
    length = len(test_array)
    for fix_ind in range(length - 1):
        for i in range(length - fix_ind - 1):
            fixed = test_array[fix_ind] 
            variable = test_array[i + 1] 
            if fix_ind != i + 1: #Impede a soma do mesmo elemento 
                test = fixed + variable 
                if test == sum:
                    return "True"
    return "False"


my_array = [1, 15, 2, 7, 2, 5, 7, 1, 4]
print ("Teste soma =  2: ", test_sum(my_array, 2))
print ("Teste soma =  1231: ", test_sum(my_array, 1231))
