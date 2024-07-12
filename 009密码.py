key = input("please:")
ans = "kfc"
l = len(key)
i = 3
while(i>0):
    k = 0
    for j in key:
        if j == '*':
            k = 1
    if k == 1:
        key = input("no * please!please:")
        #奇怪的bug点：input前没加key = 
    else:
        if ans == key:
            print("right")
            i = -1
        else:
            key = input("wrong,please:")
            i-=1
if i == 0:
    print("no")
