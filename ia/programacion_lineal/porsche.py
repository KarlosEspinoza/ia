import scipy.optimize as so

resultado = so.linprog( [50, 80], A_ub=[[5, 2],[-10, -12]], b_ub=[20, -90])

if resultado.success:
    print(f"La maquina X1 tiene que trabajar {resultado.x[0]} horas")
    print(f"La maquina X2 tiene que trabajar {resultado.x[1]} horas")
else:
    print("No hay solucion")
