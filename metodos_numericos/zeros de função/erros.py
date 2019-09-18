from math import trunc

def eabs(x1,x2):
        return float(abs(x1-x2))
def er(x1,x2):
        return float(abs((x1-x2)/x1))

class pf:
    
    """ 
        numero: numero a ser representado
        digitos: ordem de representacao no sistema de ponto
        flutuante

    """
    
    def __init__(self,numero,digitos):
        self.truncamento, self.arredondamento=self.insere_numero(numero,digitos)
        
    def insere_numero(self,pf,digitos):
             
        #Entrada de dados
    #    pf=input('Entre um número de ponto flutuante: \n')
    #    digitos=int(input('Entre a digitos de representação que você gostaria de ter do número: \n'))

        #O python automaticamente arredonda, mas como eu prefiri evidenciar a 
        #o arredondameto deixei com o formato round
        #Resolvi o truncamento de um número de vários digitos utilizando
        #O truncamento de um dígito através de potencias de 10 do número de dígitos

        trunca=lambda n,dig:float(trunc(10**dig*n)/(10**dig))

        self.truncamento=trunca(float(pf),digitos)
        self.arredondamento=round(float(pf),digitos)

        try:
            print('O truncamento do número é : {trunc}\nE o arredondamento é: {roun}'.format(trunc=self.truncamento, roun=self.arredondamento))
        except ValueError: 
            print('Desculpe, você entrou com um formato diferente')

        return self.truncamento, self.arredondamento
    


#testes com a classe 

a=pf(1/3,6)
b=pf(0.001,6)


soma_trunc=[a.truncamento for i in range(1,6)]
soma_trunc=sum(soma_trunc)
soma_arred=sum([a.arredondamento for i in range(1,6)])
total_trunc=pf(soma_trunc,6).truncamento
total_arred=pf(soma_arred,6).arredondamento
s=pf(total_trunc+b.truncamento,6)
print(er(sum([1/3 for i in range(1,6)])+0.001,total_trunc+b.truncamento))
print(er(sum([1/3 for i in range(1,6)])+0.001,total_arred+b.arredondamento))
