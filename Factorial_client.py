import Pyro4

def main():
    # Conectar al servidor
    calculator = Pyro4.Proxy("PYRONAME:example.factorial")

    # Solicitar un número al usuario
    n = int(input("Introduce un número para calcular su factorial: "))
    try:
        result = calculator.factorial(n)
        print(f"El factorial de {n} es {result}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
