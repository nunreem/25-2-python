import os

base_dir = os.path.dirname(__file__)

infilename = os.path.join(base_dir, input("입력할 파일 이름: "))    # 예: sales.txt
outfilename = os.path.join(base_dir, input("출력할 파일 이름: "))   # 예: summary.txt


sum = 0
count = 0

with open(infilename, "r", encoding="utf-8") as infile, \
     open(outfilename, "w", encoding="utf-8") as outfile:

    for line in infile:
        dailySale = int(line)  
        sum += dailySale
        count += 1

    outfile.write("총 매출 = " + str(sum) + "\n")
    outfile.write("평균 매출 = " + str(sum / count))

