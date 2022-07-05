# F_{n}=F_{n-1}+F_{n-2}
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

# Fibonacci using list

def fib1(num):
    result = []
    sum = 0
    for i in range(num + 1):
        if i > 1:
            sum = result[i-1] + result[i-2]
            result.append(sum)
        else:
            result.append(i)

    print(result)


fib1(20)


# Fibonacci using generators

def fib2(num):
    a = 0
    b = 1
    for i in range(num + 1):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib2(20):
    print(x)
