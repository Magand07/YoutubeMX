import os
"""  
    Read a file, separete lines , words and identify type of word, S= string N = number
    Don´t open archive with incorret extension, only documents .csv
    Suggests a pattern reading a one and second line of file if the user decides    
                                                                                J-Code
"""
## To develope:
## identify numbers with exponents, signs and points

def openFile(src):
    ##try:
    file = open(src,"rt")
    print(" Abriendo archivo ....",src)
    header(file,src)
    #except:
    #print(" No se pudo leer el archivo :( ")

def starting():
    archivo = ""
    print(" CONSISTENCIA DE ARCHIVOS CSV ")
    print(" Ruta del archivo : ")
    archivo = input()
    lon = len(archivo)
    type =lon-3
    ext = ""
    for i in range(type,lon):
    #print (i)
        ext = ext+archivo[i]
    #print (ext)
    if(ext != 'CSV' and ext != 'csv' and ext != 'Csv'):
        print(" Extension de archivo incorrecta ")
    else:
        openFile(archivo)
        #try:
        #except:
        #   print("EXCEPTION******  Not found! ")

def header(file,archivo):
    os.system('cls')
    print(" El archivo contiene algun encabezado? ")
    head = input()
    #all = len(file.readlines())
    if head=='si' or head=='Si' or head=='SI' or head=='sI':
        os.system('cls')
        print(" Quieres ver la sugerencia de patron? ")
        res = input()
        os.system('cls')
        if(res == 'si' or res == 'Si' or res == 'SI' or res == 'sI'):
            #print("Leyendo primera y segunda linea para detectar algun patron")
            header = 1
        else:
            header = 1 #sin sugerencia y no contar primera linea
    else:
        header = 0 #contar desde la primera linea
    patern(header,file,archivo)

#file,start line ,number of all lines ,layout
def readCSV(file,header,patron,archivo):
   # print("lONGUITUD DE PATRON: ",len(patron))
    file = open(archivo,"rt")
    count = 0 #contador de matches
    i = 0 #contador de lineas
    if(header==2):
        out = header
        # revisar desde la segunda linea hasta la ultima (sin el encabezado)
        while (True):
            i = i + 1 #contar las lineas que se leen
            line = file.readline()
            resp = separateWords(line)  # obtengo las palabra
            mimic = pattern(resp)
            #print("Patron de renglon: ", mimic)
            if (compare(mimic, patron) == 1):
                count = count + 1
            if not line:
                break
    else:
        #contar desde la segunda linea
        out = header
        #print("no puedo contar el encabezado")
        #print("Numero de lineas: ", all)
        while (True):
            i = i + 1  # contar las lineas que se leen
            line = file.readline()
            resp = separateWords(line)  # obtengo las palabra
            mimic = pattern(resp)
            #print("Patron de renglon: ", mimic)
            if (compare(mimic, patron) == 1):
                count = count + 1
            if not line:
                break
    file.close()
    i = i - out -1 #! i have a one line blank ... but why?
    percent = (count / i) * 100
    os.system('cls')
    print("Numero de lineas revisadas: ",i)
    print("PORCENTAJE DE CONSISTENCIA : ",percent)
    print("Renglones de acuerdo al patron : ",count)

def patern(header,file,archivo):
    if(header == 2): #tengo que sacar el patron de sugerencia
        patron = LearnPatron(file,archivo)
        print(" Patron sugerido :  ",patron)
        print(" Ingrese el patron a buscar: ")
        resp = input()
        os.system('cls')
        readCSV(file,header,resp,archivo)
    elif (header == 1):
        print(" Ingresa tu patron sin espacios : \n S -> Cadena \n N -> Numero \n D -> Fecha ")
        patron = input()
        #print(patron)
        #p = createPatron(patron)
        readCSV(file,header,patron,archivo)
    elif (header == 0):
        print(" Ingresa tu patron sin espacios: \n S -> Cadena \n N -> Numero \n D -> Fecha ")
        patron = input()
        print(patron)
        #p = createPatron(patron)
        readCSV(file,header,patron,archivo)


#how many ',' ,words-1
def countSign(row):
    c = 0
    for i in range(len(row)):
        if(row[i]==','):
            c = c + 1
    return c + 1

#take words in array to diference Num or String
#devuelve otro array con N, S o (D)
def pattern(words):
    r = []
    lon = len(words)
    i = 0
    if(lon != 1):
        while  i < lon :
            if (words[i].isdigit()):
               # print(i," WORD: ",words[i]," es numero")
                r.append('N')
            elif(words[i] == "-" or words[i]=="+"):
                r.append('N')
            else:
                #print(i," WORD: ",words[i]," es letra")
                r.append('S')
            i = i + 1
    return r
#take 2 patterns and verify if are the same
def compare(res,patron):
    good = 0
    if(len(res)==len(patron)):
        for i in range(len(patron)):
            if(res[i] == patron[i]):
                good = good + 1 #palomita por casilla
    if good == len(patron):
        return 1
    else:
        return 0
#write a row
#array clean with only words
def separateWords(row):
    i = 0
    j = 0
    word = ""
    words = []
    #print("Palabras: ",countSign(row))
    #print("Longuitud de frase: ",len(row))
    for i in range (len(row)):
        if(row[i]==','):
            i = i + 1
            words.append(word)
            word = ""
        else:
            if(row[i]!= "" and row[i]!= " " and row[i] != "\n" and row[i]!= "\"" and row[i]!="\'"):#fixed: special characters be ignore, if you dont have cleean before
                word = word+row[i]
            #print(" letter : ",row[i]," num: ",i)
    words.append(word) #maldita sea mi logica... podria haber hecho esto todo el tiempo
    #print(words)
    return words
#recibe una palabra retorna que tipo es , numero o cadena
def wordType(row):
    if row.isdigit():
        return 'N'
    else:
        return 'S'

#Read a first line of file an array, and detect what type is each word
#the diference with readCSV is, they open and close file, don't see all file
def LearnPatron(file,archivo):
    firstRow = file.readline()
    words = separateWords(firstRow)
    print(" Encabezado encontrado: ")
    print(words)
    secondRow = file.readline()
    words = separateWords(secondRow)
    file.close()
    file = open(archivo, "rt")
    patron = []
    for i in range(len(words)):
        patron.append(wordType(words[i]))
    return patron

def readLine(file):
    while (True):
        line = file.readline()
        words = separateWords(line)
        if not line:
            break
    return words

#toDebug:
#starting()