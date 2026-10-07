clrs = [] 
count = int(input("Enter the number of colors:")) 
print("Enter the colors:") 
for x in range(count): 
    color = input() 
    clrs.append(color)
print("first color:",clrs[0],"lastcolor:",clrs[count-1])
