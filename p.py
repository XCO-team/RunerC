import os
a=""
aq = ["gcc ","c",".c","./a.out"]

f = open("ros.txt", "a")
aq[1]=input("(if you dont have Enter) new comment : ")
a=aq[1]
if a == "":
    f = open("ros.txt", "r")
    a= f.read()
    e1= aq[0]+aq[1]+aq[2]
    e2= aq[3]
    os.system(e1)
    print("****************")
    os.system(e2)
else:
    os.remove("ros.txt")
    f = open("ros.txt", "a")
    f.write(a)
    f.close()
    f = open("ros.txt", "r")
    a= f.read()
    e1= aq[0]+aq[1]+aq[2]
    e2= aq[3]
    os.system(e1)
    print("****************")
    os.system(e2)
