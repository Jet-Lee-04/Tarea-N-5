# Proyecto calculadora 

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Función principal
def calculadora():
    print("===== CALCULADORA BÁSICA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    while True:
        opcion = input("\nElige una operación (1-5): ")
        
        if opcion == '5':
            print("¡Hasta luego!")
            break
            
        if opcion not in ['1', '2', '3', '4']:
            print("Opción no válida. Intenta de nuevo.")
            continue
            
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == '1':
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {restar(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {dividir(num1, num2)}")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()
