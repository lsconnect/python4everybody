sumEven = 0
sumOdd = 0

n = 1
while n <= 20:
    calc = n * n
    print(calc)

    if (calc % 2) == 0:
        sumEven = sumEven + calc
    else:
        sumOdd = sumOdd + calc
    n = n + 1

if n == 20:
    print("End of iteration")

print("Soma dos quadrados pares:", sumEven)
print("Soma dos quadrados ímpares:", sumOdd)
