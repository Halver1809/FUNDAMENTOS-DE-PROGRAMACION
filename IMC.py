# Calcular el indice de masa corporal (IMC)

def imc(estatura, peso):

 return peso/ estatura**2

peso= float(input('Escriba su peso (kg): '))
estatura= float(input('escriba su estatura (m): '))

indice = peso / estatura ** 2
#numero de decimales a mostrar
print(" Su IMC es " + str (round(indice,2)))
if indice >=0 and indice <= 16.9:
   print('te encuentras en delgadez severa')
elif indice >=17.0 and indice <= 18.4:
   print ('te encuentras bajo de peso')
elif indice >= 18.5 and indice <= 24.9:
   print('te encuentras normal')
elif indice >= 25.0 and indice <= 29.9:
   print('te encuentras en sobre peso')
elif indice >= 30.0 and indice <= 100:
   print('Te encuentras obeso')

