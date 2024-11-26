def main():
    guau(obten_numero())

def obten_numero():
    while True:
        n = int(input("Cuantas veces ladro?: "))
        if n > 1:
            return n

def guau(k):
    for _ in range(k):
        print("guau!!!")

main()

