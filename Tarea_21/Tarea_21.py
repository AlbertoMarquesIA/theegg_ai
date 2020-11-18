def fDivisores(NumeroIntroducido):
    Divisores = []
    for Divisor in range(NumeroIntroducido+1):
        if Divisor != 0 and NumeroIntroducido%Divisor == 0:
            Divisores.append(Divisor) 
    return Divisores
def fDCMax(DNumeroIntroducido,DDiezMil):
    Comunes = []
    for DivisoresA in range(len(DDiezMil)):
        for DivisoresB in range(len(DNumeroIntroducido)):
            if DDiezMil[DivisoresA] == DNumeroIntroducido[DivisoresB]:
                Comunes.append(DDiezMil[DivisoresA])
    return Comunes[-1]
'''pito = fDivisores(10000)
polla = fDivisores(7500)
cdm = fDCMax(polla,pito)
a = int(10000 / cdm)
b = int(7500 /cdm)
print(f"{pito} y {polla} y {cdm} y {b}/{a}")
'''
#i = 1
#while i != 0:
snumero = input()
fnumero = float(snumero)
Numerador = fnumero * 10000
inumero = int(Numerador)
 #   if fnumero > 0.00 or fnumero < 1.00:
 #       i = 0
DNumerador = fDivisores(inumero)
DDenominador = fDivisores(10000)
DCMax = fDCMax(DNumerador,DDenominador)
NumReducido = inumero / DCMax
DenReducido = 10000 / DCMax
iNR = int(NumReducido)
iDR = int(DenReducido)
print (f"{iNR}/{iDR}")
#  else:
#     i = 1'''