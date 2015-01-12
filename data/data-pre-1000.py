import os,sys


def get_header():
    f = open("attr.txt", "r")
    lines = f.readlines()
    f.close()

    attrs = list()
    for line in lines:
        attrs.append(line.split("\t")[0])

    attrs = attrs[3:]
    attrs.append("ischeat")

    header = "\t".join(attrs) + "\n"

    attrs_type = "continuous\t" * (len(attrs) - 1)
    attrs_type += "1 0\n"

    header += attrs_type

    attrs_3 = "\t" * (len(attrs) - 1)
    attrs_3 += "class\n"

    header += attrs_3

    return header
def do_main():
    f = open("training-target-a.txt","r")
    uins = f.readlines()
    f.close()

    uins = [x.strip() for x in uins]

    cnt = 0

    header = get_header()
    f = open("training.txt","r")
    fo = open("training-2.txt","w")
    fo.write(header)
    while True:
        line = f.readline()
        if not line:
            break

        parts = line.strip().split("\t")
        #print len(parts)
        uin = parts[2]
        #print uin
        if not uin in uins:
            line = '\t'.join(parts[3:75]) + "\t" + "0\n"
        else:
            line = '\t'.join(parts[3:75]) + "\t1\n"
            
        #print (len(line.split("\t")))
        cnt = cnt + 1
        fo.write(line)
        if cnt >= 1000:
            break

    fo.close()
    f.close()
    print cnt

    cnt = 0
    f = open("test.txt","r")
    fo = open("test-2.txt","w")
    fo.write(header)
    while True:
        line = f.readline()
        if not line:
            break

        parts = line.strip().split("\t")
        #print len(parts)
        uin = parts[2]
        #print uin
        if not uin in uins:
            line = '\t'.join(parts[3:75]) + "\t" + "0\n"
        else:
            line = '\t'.join(parts[3:75]) + "\t1\n"
        fo.write(line)
        cnt = cnt + 1
        if cnt >= 1000:
            break

    fo.close()
    f.close()
    print cnt

    print "uin count:%d" % len(uins)
if __name__=="__main__":
    do_main()