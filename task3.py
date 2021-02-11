#Q no -1
def Series(n):
    for i in range(1,n+1):
        if i%2:
            print(i*i+1)
        else:
            print(i*i-1)

Series(20)

