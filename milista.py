
# ejemplo de uso de listas
misnovios = ["Emma", "BEto" ,"Meny"] 
misnumeros= [6, 4, 1]
# Mostrando mis novias
print(misnovios)
# Mostrando mis numeros
print(misnumeros)
print ("--accediendo a los elmentos de la lista--")
print(misnovios[0])
if "Emma" in misnovios:
    print("si, 'Emma' esta en la lista de mis novios")
else:
    print ("no eres mi novio")
print ("numero de novios ") 
nnovios=len(misnovios)
print(f"Numero de novios = {nnovios}")
print("ciclo for")
posicion=0
for medianaranja in misnovios:
    print(posicion, " ", medianaranja)
    posicion= posicion+1