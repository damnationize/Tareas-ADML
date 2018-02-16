def numpalindromo(x):
    
    numero = str(int(x))
    
    num = numero*10
    
    i = len(numero)
    
    rnum = []
    
    rnum.append(x)
    
    for k in range(0,(i)):
        
        if (k%2) == 0:
            
            s = int(num[k])
            
            if (s%2) == 0:
        
                r = (1)*int(num[s:s+i])
            
            else:
                
                r = (1)*int(num[(-s-i):(-s)])
        
            rnum.append(r)
        
        if (k%2) == 1:
            
            s = int(num[k])
            
            if (s%2) == 0:
        
                r = ((-1))*int(num[(s):(s+i)])
            
            else:
                    
                r = ((-1))*int(num[(-s-i):(-s)])
            
            rnum.append(r)
            
    return sum(rnum)


def NumTurbo(n):

    contador = 0

    for k in range(1,n+1):
        
        c1 = str(abs(numpalindromo(k)))
        
        c2 = c1[::-1]
        
        if (c1 == c2):
            
            contador += 1
            
    
    return contador       


print(NumTurbo(200000))