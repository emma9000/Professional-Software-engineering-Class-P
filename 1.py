def factorial():
    num=int(input("Please inter a integer number"))
    result = 1
    i=num

    while i>1:
        result*=i
        i-=1

    print(f"{num} result is {result}")

res= factorial()


