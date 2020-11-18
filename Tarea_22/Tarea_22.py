a_Pesos = []
a_Produccion = []
N_Vacas = 0
Peso_Max = 0.0
def IntroduccionDatos():
    global N_Vacas
    global Peso_Max
    global a_Pesos
    global a_Produccion
    N_Vacas = int(input("Introduzca la cantidad de vacas disponibles:  "))
    Peso_Max = float(input("Introduzca el peso máximo del camión:  "))
    for CadaVaca in range(N_Vacas):
        Peso = float(input("Peso de la vaca {}:  ".format(CadaVaca+1)))
        a_Pesos.append(Peso)
        Produccion = float(input("Producción de la vaca {}:  ".format(CadaVaca+1)))
        a_Produccion.append(Produccion)
IntroduccionDatos()
print(a_Pesos)
print(a_Produccion)