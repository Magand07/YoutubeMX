"""
file to insert more than 28000 registers
***the entry file should be csv utf8
                           J-CODE
"""
import codecs
from reglas import separateWords

#generate statement 'insert into ' and take de columns to complete the statement
# # # insert into (column1,column2,colum....) values
def insert(tabla,columnas):
    sql = "insert into "+ tabla + " ('"+columnas[0]
    i = 1
    while (i < (len(columnas)-1)):# fixed
        #print(i)
        sql = sql +"','"+ columnas[i]
        i = i + 1
    sql = sql + "') values "
    print(sql)
    return sql

# group all row of values
def insertData(archivo,tabla,columnas):
    script = open("script.sql","a",encoding="utf8")
    file = open(archivo,"rt",encoding="utf8")#fixed
    i = 0
    p = 1
    all = insert(tabla,columnas)
    while (True):
        line = file.readline()
       # print(line)
        if (line != "  " or line != "" or line!= " "):
            arrPalabras = separateWords(line)
            all = all + row(arrPalabras)
            i = i + 1  # count lines reading
            if(i >= 10000):
                i = 0 # renew count
                p = p+1
                print("Parte: "+str(p)+"\n Lineas totales: ",str(p*10000))
                all = all + ";"+"\n"
                all = all.replace(",(''),", "")
                all = all.replace("ï»¿", "")
                script.write(all)
                all = insert(tabla,columnas) #toDo : quizas cada 10 deberia estar liberando esta var
            else:
                all = all + ','+ "\n"
        if not line:
            all = all + ";" + "\n"
            all = all.replace(",(''),", "")
            all = all.replace("ï»¿", "")
            script.write(all)
            break
    file.close()
    script.close()
    print("Terminado")
    # remove a empty string
    # '2014','male'),(''),;
    #all = all.replace(",(''),","")
    #all = all.replace("ï»¿","")
    #upload(all)

# returns a part of 'values ' on insert -> values ('a','b','c'),
def row(arr):
    r = "('" + arr[0]
    i = 1
    while (i<len(arr)):
        r = r +"','"+ arr[i]
        i = i + 1
    r = r + "')"
    return r

# execute the query, actually i think more in a try-catch to know whats  is broken
def upload(sql):
    script = open("sql/script.sql","w")
    script.write(sql)
    # to test : print(sql)
    script.close()
"""
    CHANGE ME : 
archivo = "videos.csv"
table = "contenidoYT"
columnas = ["title","channel","category_id","views int","likes","dislikes","comments"]
insertData(archivo,table,columnas)
"""


"""
ToDo: 
   - Write a function to create a table with columns taking reglas.py
"""