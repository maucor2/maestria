##from time import sleep
##from progress.spinner import MoonSpinner
import sys
## A
##Definir un numero primo
def es_primo(n):
    # Comprobamos si n es 2 (unico primo par)
    if n == 2:
        return True

    # Comprobamos si es menor de 2 o es par
    if n < 2 or not n % 2:
        return False

    # Comprobamos si es divisible entre cualquier entero impar entre 3 y sqrt(n)
    return not any(n % i == 0 for i in range(3, int(n**0.5) + 1, 2))

##B
# funcion de productos 
def m(n): 
    producto = 1
    while (n != 0): 
        producto = producto * (n % 10) 
        n = n // 10
    return producto

##C
#revierte los caracteres 
def r(val):
    rev = ''
    rev = (str(val)[::-1])
    return rev 

## variable globales        
    
list_primos =[]
sheldon_list = []

# esta funcion revisa si en el orden de la lista la multiplicacion entre los digitos es igual a la posicion de la lista
def lista_primo (num):
    #with MoonSpinner('Revisando primos…') as bar:
        
        pos_lista_primo = 0 #variable de conteo
        primo = 1 #valor evaluado
        multi_digi = 0 #numero de multiplicacion
        
        while pos_lista_primo < num:
            
            primo +=1
            v = False 
            if es_primo(primo):
                pos_lista_primo +=1
                multi_digi = m(primo) 
                if multi_digi == pos_lista_primo:#verifica si el producto es v
                    v = True
                    
                    #print([c, val, m_p, v])
                    
                    sheldon_list.append([pos_lista_primo, primo, multi_digi, v])
                list_primos.append([pos_lista_primo, primo, multi_digi, v])
                #sleep(0.15)
                #bar.next()
                #print(pos_lista_primo, primo, multi_digi, v)
                progress = pos_lista_primo/num*100
                sys.stdout.write("Progrso de análisis: %d%%   \r" % (progress) )
                sys.stdout.flush()
        #print(sheldon_list)
        

        for i in sheldon_list:
            
            #print(list[int(r(i[0]))-1][1],int(r(i[1])),i[1])
            inv_num_lista = r(i[0])
            inv_primo = int(r(i[1]))
            if list_primos[int(inv_num_lista)-1][1]==inv_primo:
                #if i[1]==73:
                print(f'\n\tSheldon tiener razon, solo {i[1]} que es el primo #{i[0]},\n\ty su pocision inversa es la #{inv_num_lista} y el numero primo\n\tinverso corresponede a  {inv_primo}\n')
            else:
                #print (f'existe el numero {i[1]} que esta en la posicion #{i[0]},\ny su posicion inversa es {inv_num_lista}pero el numero en esa\npocision es {list[int(inv_num_lista)-1][1]} y no es el inverso {inv_primo}\n')
                print (f'\n\texiste el numero {i[1]} que esta en la posicion {i[0]},\n\ty su posicion inversa es {inv_num_lista}pero el numero en esa\n\tpocision es {list_primos[int(inv_num_lista)-1][1]} y no es el inverso {inv_primo}\n')
    
        


print("Sheldon Cooper, cree que el 73 es el mejor número, \ndice que es el primo número 21 y el inverso de 21\nosea 12, es 37 el inverso de 73, quiere probar la\nteoría de sheldon? ingrese cuantos números primos \nquiere revisar: (si deja el espacio vacio se\nrevisaran 1.000.000 números primos, este proceso\n puede tomar varios minutos)")
x = input()
if x == '':
    x=1000000
else:
    x = int(x)

lista_primo (x)
k=input("Presione una tecla para cerrar") 

