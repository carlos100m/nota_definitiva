# Programa para calcular el area y el perimetro de un circulo de Radio R

# Librerias
import math

print ("--------------------------------------------")
print ("Nota Definitiva de una asignatura")
print ("--------------------------------------------")

# --------------------------------------------------------------------------
# Input
# --------------------------------------------------------------------------

nc=int(input("Digite el valor de la nota cognitiva: "))
np=int(input("Digite el valor de la Nota Procedimental: "))
na=int(input("Digite el valor de la Nota Actitudinal: "))
au=int(input("Digite el valor de la Nota Autoevaluacion: "))
bi=int(input("Digite el valor de la Nota Bimestral: "))

# --------------------------------------------------------------------------
# Proceso
# --------------------------------------------------------------------------

nd=0.3*np+0.1*na+0.1*au+0.2*bi

# --------------------------------------------------------------------------
# Salida
# --------------------------------------------------------------------------

print("---------------Resultado------------------")
print("El valor de la Nota definitiva de la asignatura es:"+str(nd))
