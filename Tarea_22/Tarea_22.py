def IntroduccionDatos():
    NVacas = int(input("Introduzca la cantidad de vacas disponibles:"))
    PesoMax = float(input("Introduzca el peso máximo del camión:"))
    aPesos = []
    aProduccion = []
    for CadaVaca in range(NVacas):
        Peso = float(input("Peso de la vaca {}:".format(CadaVaca+1)))
        aPesos.append(Peso)
        Produccion = float(input("Producción de la vaca {}:".format(CadaVaca+1)))
        aProduccion.append(Produccion)

IntroduccionDatos()