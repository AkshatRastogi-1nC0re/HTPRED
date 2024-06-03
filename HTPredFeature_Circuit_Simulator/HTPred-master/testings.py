f = open("headers.txt", "r")
x = f.read()
f.close()


listx = x.split(",")
print(listx)

listy = []
for i in listx:
    xx  = i
    xx.strip(" ")

print(listy)