"""
Programa para generar arrays desde documentos csv
                            J-CODE
"""

#for a number column of file.csv saves into array
#starts on 0
def columnaToArray(numColumn,archivo):
    i = 0
    arr = []
    file = open(archivo,"rt",encoding="utf8")
   # print("abriendo archivo : ",archivo)
    while (True):
        i = i + 1
        line = file.readline()
        try:
            #    print(line)
            #    print("Linea leida: ", i)
            resp = separateWords(line)  # obtengo las palabras
            if(numColumn<countSign(line)):
                arr.append(resp[numColumn]) #guardo solo la palabra buscada
        except:
            print("Linea no leida: ",i," contenido: ",line)
        if not line:
            break

    file.close()
    return arr

#take a string, separate on words
#returns arrary with 'n' words
def separateWords(row):
    i = 0
    word = ""
    words = []
  #  print("Palabras: ",countSign(row))
   # print("Longuitud de frase: ",len(row))
    for i in range (len(row)):
        if(row[i]==','):
            i = i + 1
            words.append(word)
            word = ""
        else:
            word = word+row[i]
            #print(" letter : ",row[i]," num: ",i)
    words.append(word) #maldita sea mi logica... podria haber hecho esto todo el tiempo
    #print(words)
    return words
#contar cuantas comas hay , osea cuuantas palabras -1 hay
def countSign(row):
    c = 0
    for i in range(len(row)):
        if(row[i]==','):
            c = c + 1
    return c + 1

#file name, needed number of columns
#for test:
#archivo = "prueba_mapas.csv"
#print(columnaToArray(1,archivo))