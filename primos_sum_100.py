

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
      
    pos_lista_primo = 0 #variable de conteo
    primo = 1 #valor evaluado
    multi_digi = 0 #numero de multiplicacion
        
    while pos_lista_primo < num:
            
        primo +=1
        v = False 
        if es_primo(primo):
            pos_lista_primo +=1
            multi_digi = m(primo) 
            list_primos.append(primo)
            sum_primos = sum(list_primos)
           
            if sum_primos< 1000:
                 print(sum_primos)
            else:
                break
           
                
        
      
    print(list_primos)




lista_primo (1000)
