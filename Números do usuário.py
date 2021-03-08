x = int(input('Primeiro valor'))
2 y = int(input('Segundo valor:'))
3 z = x / y
4 print('O resultado da divisao e:', z)
'''
repetir=True
while repetir:
    try:
        x = int(input('Primeiro valor:'))
        y = int(input('Segundo valor: '))
        z = x / y

    except ValueError:
         print('Atenção, os valores devem ser inteiros')
    except ZeroDivisionError:
         print('Atenção, os valores devem ser diferentes de zero')
    except:
         print('Atenção, erro inesperado aconteceu')
    else:
         print('O resultado da divisão e: ', z)
         repetir=False
