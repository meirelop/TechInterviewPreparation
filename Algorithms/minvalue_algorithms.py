import math

## Finding minimum value of function, in given interval with 3 different methods

# Given function, can be changed
def func(u):
    return (-math.e**-u) * math.log(u)


# 1. Dichotomy method
def dichotomy(a, b, epsilon):
    while (abs((b - a)) >= epsilon):
        sigma = epsilon / 2.1
        lyambda = ((a + b) / 2) - sigma
        mu = ((a + b) / 2) + sigma
        if func(lyambda) < func(mu):
            b = mu

        elif func(lyambda) > func(mu):
            a = lyambda

    min_nukte = (a+b) / 2
    print('Dichotomy minimum:', min_nukte)
    return min_nukte


# Golden section method
def altyn_kima(a, b, epsilon):
    gamma = 0.618
    while (abs(b-a) >= epsilon):
        lyambda = a + (1-gamma) * (b-a)
        mu = a + gamma * (b - a)
        if func(lyambda) <= func(mu):
            b = mu
            mu = lyambda
            lyambda = a + (1-gamma) * (b-a)
        else:
            a = lyambda
            lyambda = mu
            mu = a + gamma * (b - a)

    min_nukte = (a+b) /2
    print('Golden section minimum:', min_nukte)
    return min_nukte


# 3. Fibonacci method
def fibonacci(a, b, epsilon):
    j = N = 20

    while(j != 2):  # j==1
        lyambda = a + fib(j-2) * epsilon
        mu = a + fib(j-1) * epsilon
        if func(lyambda) < func(mu):
            b = mu
            mu = lyambda
            lyambda = a + fib(j-2) * epsilon
        else:
            a = lyambda
            lyambda = mu
            mu = a + fib(j-1) * epsilon
        j = j-1

    min_nukte = (a+b) / 2
    print("Fibonacci minimum:", min_nukte)
    return


def fib(n):
    # Calculating fibonacci sequence
    if n < 0:
        return
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)



def main():
    dichotomy(a=-1, b=3, epsilon=0.01)
    altyn_kima(a=-1, b=3, epsilon=0.01)
    fibonacci(a=-1, b=3, epsilon=0.01)


main()



