import csv,operator

def leer_archivo():
    
  
   #with open('C:\\Users\\kenne\\Documents\\UAM\\Progra Avanzada\\ICE\\ArchivoMediciones\\mediciones.csv') as mi_archivo_leido:
       # reader = csv.reader(mi_archivo_leido)
       # for row in reader:
           # print(row)
    #return reader

  output = [] 
  f = open('C:\\Users\\kenne\\Documents\\UAM\\Progra Avanzada\\ICE\\ArchivoMediciones\\mediciones.csv')
  for line in f:
    cells = line.split(";")
    
    output.append([(cells[1]),(cells[2])])
  f.close

  print(output)




"""obj_reader=leer_archivo
def separarDatos(reader):
    lista=sorted(reader,key=operator.itemgetter(1))
    print(lista) """


leer_archivo()
