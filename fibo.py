def fibo(n):

    f0 = 0

    f1 = 1

    f_ne = f0 + f1

    f_n1 = f1

    #Sumando los primeros f1 y f2 que son impares, iniciamos ftotal = 2, que es la suma.

    ftotal = 2

    while (f_ne < n):

        f_n0 = f_n1

        f_n1 = f_ne

        f_ne = f_n1 + f_n0

        k = f_ne % 2

        if k == 1:

            ftotal += f_ne

    return ftotal



        
print(fibo(100000))
        