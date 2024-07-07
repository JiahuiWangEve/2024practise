def f(num):
    x = 1
    if num > 2:
        x = f(num-1)+f(num-2)
    return x
print(f(int(input("你想知道第几位？"))))
#水一节

    
