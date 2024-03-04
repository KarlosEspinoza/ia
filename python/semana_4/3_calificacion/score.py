score = int(input("Ingresa calificacion: "))

#[90 100] A
if score >= 90 and score <= 100:
    print("Tu calificacion es una A")
#[80 90) B
elif score >= 80 and score < 90:
    print("Tu calificacion es una B")
#[70 80) C
elif score < 80 and score >= 70:
    print("Tu calificacion es una C")
#[60 70) D
elif score < 70 and score >= 60:
    print("Tu calificacion es una C")
#menos de 60 F
else:
    print("Tu calificacion es una F")
