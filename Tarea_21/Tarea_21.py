def fDivisores(NumeroIntroducido):                  #Funcion encargada de obtener los divisores de un valor Input
    Divisores = []
    for Divisor in range(NumeroIntroducido+1):
        if Divisor != 0 and NumeroIntroducido%Divisor == 0:
            Divisores.append(Divisor) 
    return Divisores                                #Devuelve un array con todos los divisores del valor introducido en orden
def fDCMax(DNumeroIntroducido,DDiezMil):            #Función encargada de obtener el Divisor común máximo de dos arrays de entrada
    Comunes = []                                    #Array en el que entrarán los Divisores comunes, siendo el último el máximo                     
    for DivisoresA in range(len(DDiezMil)):
        for DivisoresB in range(len(DNumeroIntroducido)):
            if DDiezMil[DivisoresA] == DNumeroIntroducido[DivisoresB]:
                Comunes.append(DDiezMil[DivisoresA])
    return Comunes[-1]                              #Devuelve el valor del Divisor común máximo que sera el último valor del array de Divisores comunes
def main():                                         #Programa principal donde se establecen las condiciones donde el valor minimo es 0.0001 y 0.9999
    i = 1
    while i != 0:
        snumero = input()
        fnumero = float(snumero)
        Numerador = fnumero * 10000
        inumero = int(Numerador)
        if fnumero > 0.00 and fnumero < 1.00:
            i = 0
            DNumerador = fDivisores(inumero)
            DDenominador = fDivisores(10000)
            DCMax = fDCMax(DNumerador,DDenominador)
            NumReducido = inumero / DCMax
            DenReducido = 10000 / DCMax
            iNR = int(NumReducido)
            iDR = int(DenReducido)
            print (f"{iNR}/{iDR}")

main()
