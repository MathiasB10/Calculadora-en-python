def ingresar_numeros():
    global a, b
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Infinito (no se puede dividir entre cero)"

def par(n):
    return n % 2 == 0

def factorial(n):
    if n < 0:
        return "No definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

historial = []

while input("¿Desea realizar una operación? (si/no): ") == "si":
    ingresar_numeros()
    operacion = input("Ingrese la operación a realizar (sumar, restar, multiplicar, dividir): ").lower()
    
    if operacion == "sumar":
        print("Resultado:", sumar(a, b))
        print("¿El resultado es par?", par(sumar(a, b)))
        print("Factorial del resultado:", factorial(sumar(a, b)))
        historial.append(("sumar", a, b, sumar(a, b)))
    elif operacion == "restar":
        print("Resultado:", restar(a, b))
        print("¿El resultado es par?", par(restar(a, b)))
        print("Factorial del resultado:", factorial(restar(a, b)))
        historial.append(("restar", a, b, restar(a, b)))
    elif operacion == "multiplicar":
        print("Resultado:", multiplicar(a, b))
        print("¿El resultado es par?", par(multiplicar(a, b)))
        print("Factorial del resultado:", factorial(multiplicar(a, b)))
        historial.append(("multiplicar", a, b, multiplicar(a, b)))
    elif operacion == "dividir":
        print("Resultado:", dividir(a, b))
        print("¿El resultado es par?", par(dividir(a, b)) if isinstance(dividir(a, b), (int, float)) else "No aplica")
        print("Factorial del resultado:", factorial(dividir(a, b)) if isinstance(dividir(a, b), int) else "No aplica")
        historial.append(("dividir", a, b, dividir(a, b)))
    else:
        print("Operación no válida.")
        
while input("¿Desea ver el historial de operaciones? (si/no): ") == "si":
    if len(historial) == 6:
        historial.remove(historial[0])
    print("Historial de operaciones:", historial)
    if input("Desea eliminar el historial completo? (si/no): ") == "si":
        historial.clear()
        print("Historial eliminado.")