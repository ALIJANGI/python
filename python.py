x = input('enter list length')
try :
    x = int(x)
except :
    print('enter a valid number')
    quit()

num = []

for i in range(x):
    n = int(input("enter a number"))
    num.append(n)

max_num = num[0]

for i in range(x):
    if(max_num < num[i]):
        max_num = num[i]

print(max_num)