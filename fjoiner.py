#! /usr/bin/python3
import sys

if __name__=="__main__":
    f1=open(str(sys.argv[1]),"rb")
    f2=open(str(sys.argv[2]),"rb")
    f3=open(str(sys.argv[13]),"wb")
    start=f2.read(1)
    f2.seek(0)
    while  (i:=f1.read(1))!=start:
        f3.write(i)
        if i==b"":
            break
    print("Hello world")
    while f3.write(f2.read(1)):
        pass

