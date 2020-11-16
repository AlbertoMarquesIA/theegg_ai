def fDivisores(NumeroIntroducido):
    Divisores = []
    for Divisor in range(NumeroIntroducido+1):
        if Divisor != 0 and NumeroIntroducido%Divisor == 0:
            Divisores.append(Divisor) 
    longitud = len(Divisores)
    Divisores.append(longitud)
    return Divisores
def fDCMax(DNumeroIntroducido,DDiezMil):
    Comunes = []
    for DivisoresA in range(DDiezMil[-1]):
        for DivisoresB in range(DNumeroIntroducido[-1]):
            if DDiezMil[DivisoresA] == DNumeroIntroducido[DivisoresB]:
                Comunes.append(DDiezMil[DivisoresA])
    return Comunes[-1]

numero = float(input())
Numerador = numero * 10000
DNumerador = fDivisores(Numerador)
DDenominador = fDivisores(10000)
DCMax = fDCMax(DNumerador,DDenominador)
NumReducido = numero / DCMax
DenReducido = 10000 / DCMax
print({NumReducido},'/',{DenReducido})

