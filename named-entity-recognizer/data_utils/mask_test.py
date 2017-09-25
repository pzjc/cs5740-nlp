
fw = open("test.masked2",'w')

with open("test.nolabels.txt") as fd:

    for line in fd:
     # new sentence on -DOCSTART- or blank line
        if len(line.strip("\n")) != 0:
            fw.write(line.strip("\n")+"\t"+"O"+'\n')
        else:
            fw.write("\n")


        # flush running buffer


