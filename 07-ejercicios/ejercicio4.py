"""
Ejercicio 4.
Pedir dos numero al usuario y hacer todas las operaciones
de una calculadora y mostrarla por pantalla
"""
# Ejercicio por Daniel Vera
print("Calculadora por numeros\n\t")
num1= int(input("Ingresa el primero numero: "))
num2= int(input("Ingresa el segundo numero: "))

suma    = num1 + num2
resta   = num1 - num2
multi   = num1 * num2
divi    = num1 / num2
resto   = num1 % num2    
expo    = num1 **num2

print(f"El resultado de la suma es: {suma}\n"
f"El resultado de la resta es: {resta}\n"
f"El resultado de la multiplicacion es: {multi}\n"
f"El resultado de la division es: {divi}\n"
f"El resultado del resto es: {resto}\n"
f"El resultado de la exponeciasion es: {expo}");