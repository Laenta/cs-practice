limit = int(input())
n=int(input())
templist=[]
uplimit = 0
mistake = 0
for i in range(n):
    temperature = input()
    if temperature == "error":
        mistake +=1
    else:  
        temperature = float(temperature)  
        templist.append(temperature)
        if temperature > limit:
            uplimit +=1

        


print(f'{max(templist):.1f}')
print(f'{sum(templist)/len(templist):.1f}')