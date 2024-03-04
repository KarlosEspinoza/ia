def main():
    x = int(input("Ingrese x: "))
    if es_par(x):
        print("es par")
    else:
        print("es impar")

def es_par(n):
    return n % 2 == 0

main()
