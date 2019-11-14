#!/usr/bin/python3

import os
files=os.listdir(r"C:\Users\yhh\Desktop\新建文件夹")
for filename in files:
    twopath = os.path.splitext(filename)
    if twopath[1] == ".c":
        newname = twopath[0]+".cpp"
        os.chdir(r"C:\Users\yhh\Desktop\新建文件夹 2")
        os.rename(filename,newname)
