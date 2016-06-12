#!/home/zhuhang-xy/python/bin/python10
#coding=utf-8
import sys
reload(sys)
import os
import string

TotalNumber = 0

def statistic(dir, tdir, tdir2):
    global TotalNumber
    files = os.listdir(dir)
    for f in files:
        if os.path.isdir(dir + "/" + f):
            continue;
        if os.path.isfile(dir + "/" + f):
            flag = 0
            input = open(dir + "/" + f, "r")
            for line in input:
                 set = line.strip().strip('\n').split(":")
                 if set[1].strip() != "":
                     flag = 1
                     set2 = set[1].split("\t")
                     TotalNumber = TotalNumber + len(set2)
            input.close()
            input = open(dir + "/" + f, "r")
            if flag == 1:
                output = open(tdir + "/" + f, "w")
                for line in input:
                    output.write(line)
                output.close()
            else:
                output = open(tdir2 + "/" + f, "w")
                for line in input:
output.write(line)
                output.close()
            input.close()
    print TotalNumber

if __name__ == "__main__":
    statistic("business_area", "business_area_has", "business_area_no")
