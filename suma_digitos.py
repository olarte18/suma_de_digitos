#input
n=int(input("Digite un valor positivo: "))
#processing
suma=0
d=n
if n>=0:
    while n!=0:
        r=n%10
        n=n//10 
        suma=suma+r
    print ("Numero digitado: "+str(d)+", Resultado suma: "+str(suma))