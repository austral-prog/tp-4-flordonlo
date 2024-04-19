def line():
    Y= "Y"
    X= "X"
    coef_A= float(input("Ingrese el coeficiente A: "))
    coef_B= float(input("Ingrese el coeficiente B: "))
    coef_X1= float(input("Ingrese el coeficiente X1: "))
    coef_X2= float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {float(coef_A)}")
    print(f"El coeficiente B de su ecuación de la recta es: {float(coef_B)}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {float(coef_X1)}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {float(coef_X2)}\n")
    print("Para la siguiente ecuación: ")
    print(f"\t{Y} = {float(coef_A)}{X} + {coef_B}\n")
    print("Dados los siguientes puntos: ")
    X1= coef_X1
    print(f"\tP1 ({float(coef_X1)}, {float(coef_A*X1+coef_B)})")
    X2= coef_X2
    print(f"\tP2 ({float(coef_X2)}, {float(coef_A*X2+coef_B)})\n")
    Y1= float(coef_A*X1+coef_B)
    Y2= float(coef_A*X2+coef_B)
    print(f"La distancia entre ellos es: {((float(X2-X1))**2+(float(Y2-Y1))**2)**(0.5)}")
line()
