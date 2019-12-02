dados=open('qg_dados.txt')
leitura=dados.read()
lista_por_ordem=leitura.split('\n\n')
bview=[elemento.split('\n') for elemento in lista_por_ordem]
traducao=bview[0][2][:3]

mapeamento={}

for n in bview:
    key=n[0]
    linhas=[]
    for string in n[1:]:
        if traducao in string:
            string=string.replace(traducao,'-')
        linhas.append(string.split(' '))
    mapeamento[key]=linhas

for arrays in mapeamento.keys():
    for row in range(len(mapeamento[arrays])):
        for col in range(len(mapeamento[arrays][row])):
            mapeamento[arrays][row][col]=float(mapeamento[arrays][row][col])

import numpy as np
mapeamento=dict(zip(list(mapeamento.keys()),[np.array(mapeamento[key]) for key in mapeamento.keys()]))



        
