#This code will converts exported .txt file from whatsapp to .csv file.

#Copy and paste your file path here inside double quotes.
# data file
file = r""
#copy of data file
file_d = r""
#new file where the result will be stored
file_n = r""

fw = open(file_n, "w", encoding='UTF-8')
fw.seek(0)
fw.truncate()
fr = open(file, "r", encoding='UTF-8')

while True:
    line = fr.readline()
    if not line:
        break
    d=0

    if "joined using this group's invite link" in line:
        index = line.index("joined using this group's invite link")
        d=1
    elif "was added" in line:
        index = line.index("was added")
        d=1
    elif "was added" in line:
        index = line.index("was added")
        d=1
    elif "joined from the community" in line:
        index = line.index("joined from the community")
        d=1
    
    line = list(line)

    if (len(line) >= 10) and (line[2] == "/") and (line[5] == "/") and (line[10] == ","):
        fw.write("\n")
        if d==1:
            line[index-2] = ":"
        p=0
        q=0
        j=0
        while (j+17 != len(line)):
            if (line[j+17] == "-") and (p == 0):
                line[j+17] = ","
                p=1
            if (line[j+17] == ":"):
                line[j+17] = ","
                q = 1
                k=0
                while (j+18+k != len(line)):
                    if line[j+18+k] == ",":
                        line[j+18+k] = "#"
                    k+=1
                break
            j+=1
        line = "".join(line)
        if q == 1:
            print(line)
            fw.write(line.replace('\n', ''))
    else:
        i=0
        while (i != len(line)):
            if line[i] == ",":
                line[i] = "#"
            i+=1
        line = "".join(line)
        fw.write(line.replace('\n', ''))
    
fr.close()
fw.close()
