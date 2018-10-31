#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/6 15:13



if __name__ == "__main__":
    f = open("test.txt","r+")
    print(f.readline())
    print(f.readline())
    f.seek(0)
    f.seek(0,2)
    for i in f:
        print(i)
    f.close()

    f = open("test.txt","w+")
    f.seek(0)
    f.write("abcd\n")
    f.write("abcd\n")
    f.write("abcd\n")
    f.write("abcd\n")
    f.flush()
    print(f.readlines())
    f.close()