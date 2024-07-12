
def code(k):
    ans = 0
    key = str(k)
    for i in key:
        j = int(i)
        #print(j)
        ans+=j**3
    #print (k,ans,key)
    if ans == k:
        print(k)
for i in range(100,1000):
    code(i)

