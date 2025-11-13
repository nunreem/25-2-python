infile=open(r"C:\Pyhton Projects\25-2-python\lecture_practice\lec_12\phones.txt","r",encoding="utf-8")
for line in infile:
    line=line.rstrip()
    print(line)

infile.close()
