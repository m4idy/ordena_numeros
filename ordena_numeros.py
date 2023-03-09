

print(".................................................................")
print("...................ordenador de numeros..........................")
print(".................................................................")

# imput

a=int(input("ingrese el primer valor"))
b=int(input("ingrese el segundo valor"))
c=int(input("ingrese el tercer valor"))

if a>b :
    if b>c :

        rta = "el orden ascendente de los números son: " + str (c)+", " + str (b)+", " + str (a)

    else :

        rta = "el orden ascendente de los números son: " + str (b)+", " + str (c)+", " + str (a)

else :

     if b<c :

         rta = "el orden ascendente de los números son: " + str (a)+", " + str (b)+", " + str (c)
 
     else :
        

        rta = "el orden ascendente de los números son: " + str (c)+", " + str (a)+", " + str (b)

if c>a :
            
    rta = "el orden ascendente de los números son: " + str (a)+", " + str (c)+", " + str (b)
else :

     rta = "el orden ascendente de los números son: " + str (b)+", " + str (c)+", " + str (a)

print (rta)
