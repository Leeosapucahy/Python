def potenciacao_em_lista(lista):
    numeros_potenciados = []
    indice = 0
    while indice < (len(lista)):
        numero_atual = (lista[indice])
        if indice == 0 or indice == (len(lista)-1):
            numeros_potenciados.append(numero_atual)
        else:
            resultado = numero_atual % 2 #par
            if resultado ==0:
                numeros_potenciados.append (numero_atual **2)
            else:
                numeros_potenciados.append (numero_atual **3) #comportamento padrao
        indice = indice + 1

    return numeros_potenciados


    
