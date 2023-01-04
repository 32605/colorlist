colorlist = []
repeat = "Y"
while repeat == "Y":
    name = input("enter a color: ")
    colorlist.append(name)
    repeat = input("Do you want to add another color?(Y/N) ")
for i in range(len(colorlist)):
    print(i, colorlist[i])