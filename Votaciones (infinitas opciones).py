import random

opciones=[]
opcion="placeholder"
i=0

while opcion!="":
  opcion=input("Ingresa un candidato o presiona Enter para empezar las votaciones\n")
  if opcion=="":
    break
  opciones.append(opcion)
  i=i+1


votantes=random.randint(100,1000000)
porcentajes=random.sample(range(5,50),i)
nulos=random.randint(1,4)

print("\n")
input("Llegaron "+str(votantes)+" votantes y el resultado fue: (presiona Enter)")
input("*Redoble de tambores* (presiona Enter)")

print("\n")

ganador=0

for j in range(0,i):
  print(""+str(opciones[j])+" obtuvo un "+"%.2f" % (porcentajes[j]/(sum(porcentajes)+nulos)*100)+"%")
  if porcentajes[ganador]<porcentajes[j]:
    ganador=j

print("\n")
print(""+"%.2f" % (nulos/(sum(porcentajes)+nulos)*100)+"% voto nulo")
print("\n")
print("\n")
print("El ganador es "+opciones[ganador]+" !")