#Dada a seguinte arvore binária de palavras, faça uma função que busque nessa arvore pela
#palavra-chave. O output da sua função deve ser o caminho até chegar no item procurado. Por
#exemplo, se o input de buscar for “goiaba” o output deve ser uma string “Maça -> morango -> Goibana”.

class BSTNode(object):
    def __init__(self, key, value=None, left=None, right=None, traceback=[]):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.traceback = traceback

    def Traceback(self):
        print(self.traceback, sep=' -> ') # não consegui fazer o sep funcionar....

    
    def get(self, key):
        #Retorna uma referência ao nó de chave key
        if self.key == key:
            self.traceback.append(self.value)
            return self.Traceback()
        node = self.left if key < self.key else self.right
        self.traceback.append(self.value)
        if node is not None:
            return node.get(key)


#Construção da árvore
#Tive que incluir chave numérica
root = BSTNode(50, value='Maça') 
root.left = BSTNode(25, value='Morango')
root.left.left = BSTNode(20, value='Goiaba')
root.left.right = BSTNode(30, value='Limão')
root.right = BSTNode(75, value='Pera')
root.right.left = BSTNode(70, value='Abacaxi')
root.right.left.left = BSTNode(60, value='Laranja')
root.right.left.left.left = BSTNode(55, value='Banana')
root.right.left.left.right = BSTNode(65, value='Cebola')

#Deverá ser inserido a chave do elemento a ser buscado
Search = root.get(20)




