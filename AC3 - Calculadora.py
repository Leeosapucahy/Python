import abc
from unittest import TestCase, main  

class operacao(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def executar(self, num1, num2):
        pass

class divisao(Operacao):
    def executar(self, num1, num2):
        conta=num1/num2
        return conta

class soma(Operacao):
    def executar(self, num1, num2):
        conta=num1+num2
        return conta

class subtracao(Operacao):
    def executar(self, num1, num2):
        conta=num1-num2
        return conta

class multiplicacao(Operacao):
    def executar(self, num1, num2):
        conta=num1*num2
        return conta

class fabrica(object):
    def criar(self, operador):
        if(operador=='soma'):
            return Soma()
        elif(operador=='divisao'):
            return Divisao()
        elif(operador=='subtracao'):
            return Subtracao()
        elif(operador=='multiplicacao'):
            return Multiplicacao()

class calculadora():
    def calcular(self, num1, num2, operador):
        fabrica=fabrica()
        operacao = fabrica.criar(operador)
        if(operacao ==None):
            return 0
        else:
            resultado = operacao.executar(num1, num2)
            return resultado

class testes_ac(TestCase):
    def teste_divisao(self):
        testarD = Calculadora()
        resultado = testarD.calcular(48,6, 'divisao')
        self.assertEqual(resultado, 8)
        print ("passou na divisão")

    def teste_soma(self):
        testarS = Calculadora()
        resultado = testarS.calcular(7,7,'soma')
        self.assertEqual(resultado, 14)
        print ("passou na soma")

    def teste_subtracao(self):
        testarMenos = Calculadora()
        resultado = testarMenos.calcular(25,24,'subtracao')
        self.assertEqual(resultado, 1)
        print ("passou na subtração")
    
    def teste_multiplicacao(self):
        testarM = Calculadora()
        resultado = testarM.calcular(3,10,'multiplicacao')
        self.assertEqual(resultado, 30)
        print ("passou na multiplicação")
 
if _name_ == '_main_':
    main()