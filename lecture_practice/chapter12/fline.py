import os

base_dir = os.path.dirname(__file__)
filepath = os.path.join(base_dir, "proverbs.txt")

infile = open(filepath)
outfile = open(filepath, "w")
i = 1


for line in infile:
    outfile.write(str(i) + ": " + line)
    i = i + 1

infile.close()
outfile.close()