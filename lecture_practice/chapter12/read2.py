infile=open(r"C:\Pyhton Projects\25-2-python\lecture_practice\lec_12\phones.txt","r",encoding="utf-8")
line= infile.readline()
while line!="":
    print(line)
    line=infile.readline()

infile.close()
