import sympy as sy
sx=sy.symbols('x')
from lendo_dados import mapeamento

f=(sx**3-2)/(sx**3-sx**2)
f1=sx**6-sx**2*sy.sin(2*sx)
f2=sy.exp(sx)*sy.cos(sx)
def quad_gaussiana(funcao,a,b,n):
    """
    Entradas

    funcao: funcao sympy de uma variável
    a:limite inferior da integral
    b:limite superior da integral
    n:inteiro da quantidade de particoes desejadas

    Retorno

    xi: Valor numérico da integral por quadratura gaussiana
    """
    eqg=lambda n:n in [2,3,4,5]#verifica grau
    u=lambda x:(2*x-a-b)/(b-a)#troca para u
    if not eqg(n):print('O grau deve ser entre 2 e 5')
    else:
        array=mapeamento[str(n)];xs=array[:,0];cn=array[:,1]
        return sum([cn[k]*funcao.subs(sx,u(xs[k])) for k in range(len(xs))])*(b-a)/2

def simpson_composicao(funcao,a,b,n):
    
    """
    Entradas

    funcao: funcao sympy de uma variável
    a:limite inferior da integral
    b:limite superior da integral
    n:inteiro da quantidade de particoes desejadas

    Retorno

    xi: Valor numérico da integral, pela composição
    de simpsom

    """

    h=(b-a)/n
    xi0=funcao.subs(sx,a)+funcao.subs(sx,b);xi1=0;xi2=0
    for i in range(n):
        x=a+i*h
        if i%2==0: xi2+= funcao.subs(sx,x)
        else: xi1+=funcao.subs(sx,x)
    xi=(h/3)*(xi0+2*xi2+4*xi1)
    return xi

def trapezio_composicao(funcao,a,b,n):
    
    """
    Entradas

    funcao: funcao sympy de uma variável
    a:limite inferior da integral
    b:limite superior da integral
    n:inteiro da quantidade de particoes desejadas

    Retorno

    xi: Valor numérico da integral, pela composição
    de trapezios

    """

    h=(b-a)/n
    xi0=funcao.subs(sx,a)+funcao.subs(sx,b);xi1=0;xi2=0
    for i in range(n):
        x=a+i*h
        xi1+=funcao.subs(sx,x)
    xi=(h/2)*(xi0+2*xi1)
    return xi

print(simpson_composicao(f,2,4,3))
print(trapezio_composicao(f,2,4,3))
print(type(simpson_composicao(f2,-1,1,3)))#???