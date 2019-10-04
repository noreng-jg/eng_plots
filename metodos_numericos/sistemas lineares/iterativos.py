import numpy as np
from math import sqrt

def erro_euclidiano(vetor, vetor_anterior):
    if len(vetor)==len(vetor_anterior):
        return sqrt(sum([(vetor[posicao] -vetor_anterior[posicao])**2 for posicao in range(len(vetor))]))
    else:
        print("Vetores possuem tamanhos diferentes")

def erro_relativo(vetor, vetor_anterior):
    if len(vetor)==len(vetor_anterior):
        return max([abs((vetor[posicao]-vetor_anterior[posicao])/vetor[posicao]) for posicao in range(len(vetor))])
    else:
        print('Vetores possuem tamanhos diferentes')

class Gauss_Jacobi:
    def __init__(self, A, B):
        self.A=A;self.B=B; self.chute_inicial=np.zeros(len(B));self.tamanho_x=len(B);self.Xs=[self.chute_inicial]

    def resolve(self, precisao=1e-5):
        self.erros_euclidianos,self.erros_relativos=[],[]
        c=np.array([self.B[i]/self.A[i][i] for i in range(self.tamanho_x)])
        d=[]
        while(True):
            d.append(np.array([[0 if i==j else (self.A[i][j]/self.A[i][i]) for j in range(self.tamanho_x)] for i in range(self.tamanho_x)]))
            self.Xs.append(c-np.dot(d[-1],np.array(self.Xs[-1]).T))
            self.erros_euclidianos.append(erro_relativo(self.Xs[-1],self.Xs[-2]))
            self.erros_relativos.append(erro_euclidiano(self.Xs[-1],self.Xs[-2]))
            if self.erros_euclidianos[-1]<precisao or self.erros_relativos[-1]<precisao:
                #satisfazer primeiro critério de parada para sair do loop
                break

class Gauss_Jordan:
    def __init__(self, A, B):
        self.A=A;self.B=B; self.chute_inicial=np.zeros(len(B));self.tamanho_x=len(B);self.Xs=[self.chute_inicial]

    def resolve(self, precisao=1e-5):
        self.erros_euclidianos,self.erros_relativos=[],[]
        c=np.array([self.B[i]/self.A[i][i] for i in range(self.tamanho_x)])
        d=[]
        
        while(True):
            d.append(np.array([[0 if i==j else (self.A[i][j]/self.A[i][i]) for j in range(self.tamanho_x)] for i in range(self.tamanho_x)]))
            x_atual=np.zeros(self.tamanho_x)
            
            for i in range(self.tamanho_x):#percorrer o X
                for j in range(self.tamanho_x):
                    if i==j:
                        pass
                    elif i>j:
                        x_atual[i]-=x_atual[j]*d[-1][i,j]
                    else:
                        x_atual[i]-=self.Xs[-1][j]*d[-1][i,j]
                x_atual[i]+=c[i]
            
            self.Xs.append(x_atual)
            self.erros_euclidianos.append(erro_relativo(self.Xs[-1],self.Xs[-2]))
            self.erros_relativos.append(erro_euclidiano(self.Xs[-1],self.Xs[-2]))
            if self.erros_euclidianos[-1]<precisao or self.erros_relativos[-1]<precisao:
                #satisfazer primeiro critério de parada para sair do loop
                break


#######Testes

A=np.array([[10,1,-1],[1,10,1],[2,-1,10]])
b=np.array([10,12,11])

inst=Gauss_Jordan(A,b)
inst.resolve()
print(inst.Xs)
inst2=Gauss_Jacobi(A,b)
inst2.resolve()
print(inst2.Xs)
