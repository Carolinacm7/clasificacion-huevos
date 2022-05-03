#los huevos de categoria A son clasificados segun su peso como:
#huevos A cuyo peso va desde los 53g hasta un peso menor de 60g
#huevos aa cuyo peso va desde los 60g hasta un peso menor de 60g 
#huevos AAA cuyo peso esta por encima de los 67 g
# y los tipos B y C como:
#Huevos B cuyo peso va desde 46g hasta un peso menor de 53g 
#huevos cuyo peso es menor de 46g


from random import uniform

listaHuevos = []

for i in range (0,500):
    listaHuevos.append(round(uniform(40,70),1))

def clasificacion_huevos( lista_huevos ):

    cantidad = len( lista_huevos )
    huevosClasificados=[{"tipo_huevos":"A","numero_huevos":0,"numero_bandejas":0},\
                        {"tipo_huevos":"AA","numero_huevos":0,"numero_bandejas":0},\
                        {"tipo_huevos":"AAA","numero_huevos":0,"numero_bandejas":0},\
                        {"tipo_huevos":"BC","numero_huevos":0,"numero_bandejas":0}]
    huevosbandeja=[30,24,12,30] 
    for i in range(cantidad):
        if lista_huevos [i]>=67:
            huevosClasificados[2]["numero_huevos"]+=1
        elif 60<=lista_huevos [i]<67:
            huevosClasificados[1]["numero_huevos"]+=1
        elif 53<=lista_huevos [i]<60:
            huevosClasificados[0]["numero_huevos"]+=1
        elif 46<=lista_huevos [i]<53:
            huevosClasificados[3]["numero_huevos"]+=1
        elif lista_huevos [i]<46:
            huevosClasificados[3]["numero_huevos"]+=1
        for i in range(len (huevosClasificados)):
            huevosClasificados[i]["numero_bandejas"]=calcular_bandejas(huevosClasificados[i]["numero_huevos"],huevosbandeja[i])
       
    return (huevosClasificados)

def calcular_bandejas(cant,bandeja):
    totalbandeja = int(cant/ bandeja)
    return totalbandeja
proceso = clasificacion_huevos(listaHuevos)
proceso[0]["numero_huevos"]+proceso[1]["numero_huevos"]+proceso[2]["numero_huevos"]+proceso[3]["numero_huevos"]


print(proceso)
