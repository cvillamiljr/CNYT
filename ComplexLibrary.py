import math
def complexSum(a,b):
    real=a[0]+b[0]
    comple=a[1]+b[1]
    
    return real,comple
def complexRest(a,b):
    real=a[0]-b[0]
    comple=a[1]-b[1]
    
    return real,comple

def complexProduct(a,b):
    real=(a[0]*b[0])-(a[1]*b[1])
    comple=(a[0]*b[1])+(a[1]*b[0])
    
    return real,comple 
def complexDiv(a,b):
    real=((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2))
    comple=((a[1]*b[0])-(a[0]*b[1]))/((b[0]**2)+(b[1]**2))

    return real,comple

def complexMod(a):
    mod=((a[0]**2)+(a[1]**2))**1/2

    return mod
def complexConj(a):
    entera=a[0]
    comple=-a[1]

    return entera,comple

def polarCartesiano(a):
    #Los angulos estan en grados
    r = a[0]
    ang = radGrados(a[1])
    v1 = r*(math.cos(ang))
    v2 = r*(math.sin(ang))
    return (v1,v2)

def cartesianoPolar(a):
    v1 = (a[0]**2 + a[1]**2)**(1/2)
    v2 = gradRadi(math.atan2(a[1],abs(a[0])))
    return(v1,v2)

def complexArg(a):
    v1 = math.atan2(a[1],a[0])
    return v1


