import LibreriaComplejos as lc

def probabilidadParticula(v1,x):
    c=0
    for i in v1:
        c+=(lc.modcomplex(i))**2
    t=c**(1/2)
    a=(lc.modcomplex(v1[x])**2)/(t**2)
    return round(a*100,2)

def amplitudTrancision(v1,v2):
    a=lc.innervector(v2,v1)
    b=lc.norma(v1)*lc.norma(v2)
    res=lc.divcomplex(a,(b,0))
    a=round(res[0],2)
    b=round(res[1],2)
    return (a,b)

def valorEsperado(m1,v1):
    a=lc.accionmatrizvector(m1,v1)
    c=lc.innervector(a,v1)
    return c

##def main():
##    v1=[(2,1),(-1,2),(0,1),(1,0),(3,-1),(2,0),(0,-2),(-2,1),(1,-3),(0,-1)]
##    v2=[(-1,-4),(2,-3),(-7,6),(-1,1),(-5,-3),(5,0),(5,8),(4,-4),(8,-7),(2,-7)]
##    v3=[(1/((2)**0.5),0),(0,1/((2)**0.5))]
##    m1=[[(2,0),(1,1)],[(1,-1),(3,0)]]
##    v=[(3,-1),(0,-2),(0,1),(2,0)]
##    print(amplitudTrancision(v1,v2))
##    print(probabilidadParticula(v,2))
##    print(valorEsperado(m1,v3))
##
##main()
