import os,sys

if __name__=="__main__":
    f = open("iris.tab","r")
    lines = f.readlines()
    f.close()

    parts = lines[0].split("\t")
    print len(parts)

    parts = lines[1].split("\t")
    print len(parts)

    parts = lines[2].split("\t")
    print len(parts)

    parts = lines[3].split("\t")
    print len(parts)