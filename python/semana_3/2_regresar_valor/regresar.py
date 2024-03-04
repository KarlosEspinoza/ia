def main():
    x = input("Ingresa x: ")
    r = cuadradito(x)
    print(f"El cuadrado de x es {r}")

def cuadradito(v):
    v = int(v)
    resultado = v * v
    return resultado

main()
