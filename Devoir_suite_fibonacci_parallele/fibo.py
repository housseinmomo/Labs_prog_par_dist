list= [5, 8, 9, 7, 8, 5, 10, 14, 15, 5, 5, 17, 5, 12, 8, 2, 16, 12, 10, 18]

def fibo(list):
    fiboList = []
    newValue = 0 
    for i in list:
        newValue += i
        fiboList.append(newValue)
    return fiboList

print(fibo(list))