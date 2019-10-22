import sympy as sy


x=sy.symbols('x')
f=-3*x**2-5*x**2+3
g1=((3*x**3-3)/5)**.5
g2=(3-3*x**2)/5
g3=(3/(3*x+5))

def fp(g,p0, tol=1e-4, n=40,ps=[]):
    try:
        ps.append(p0)
        for i in range(1,n):
            p=g.subs(x,p0)
            ps.append(p)
            if abs((p-p0)/p)<tol or abs(f.subs(x,p))<tol:
                break
            p0=p
        return ps
    except TypeError:
        print('A função de entrada não converge')
 

print(fp(g3,0))
