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

def complexConver(a):

    mod=complexMod(a)
    tetha=math.atan(a[1]/a[0])
    real= math.cos(tetha)
    comple= math.sin(tetha)

    return mod,real,comple
def complexArg(a):

    if(a[0]==0 ):
        arg=0
    elif(a[0]<0 and a[1]>0):
        arg= math.atan(a[1]/a[0])
        arg=arg+(math.pi /2)
    elif(a[0]<0 and a[1]<0):
        arg= math.atan(a[1]/a[0])
        arg=arg-(math.pi /2)
    return arg

def main():
    a=(10,5)
    b=(2,5)
    print(complexDiv(a,b))
main()

