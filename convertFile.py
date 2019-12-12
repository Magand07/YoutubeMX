"""
Little funtion to read a json, identified some attributes and filter
                                                        J-Code
"""

#define what word searching and take his value
def id(line):
    num = "0"
    posId = line.find("\"id\"")
    if(posId != -1):
        posId = posId + 7
        if(line[posId+1]!= "\""):
            num = line[posId] + line[posId+1]
        else:
            num = line[posId]
        return num
    else:
        return ""

#maybe you want change this:
def title(line):
    rest = ""
    posId = line.find("\"title\"")
    if(posId != -1):
      #  print(posId)
        posId = posId +10
        rest = line[posId:len(line)]#maybe get an error
      #  print("nombre: ",rest)
        last = rest.find("\"")
      #  print(last)
        rest = rest[0:last]
     # print(rest)
        return rest
    return rest
#to change json to sql, inserts only i want
def write(newFile,file):
    string = ""
    fopen = open(file, "rt")
    while (True):
        line = fopen.readline()
        if(id(line)!= ""):
            print(id(line))
            string = string + "insert into categoryVideo(categori_id,category) values ('"+id(line)+"','"
        if(title(line)!= ""):
            print(title(line))
            string = string + title(line)+ "');" +"\n"
        if not line:
            break
    fopen.close()
    script = open(newFile, "w")
    script.write(string)
    script.close()

"""
main: 
file = "MX_category_id.json"
newFile = "categorias.sql"
write(newFile,file)
"""