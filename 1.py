def calc():
    sum1 = 0
    count = 0
    for i in range(1, 1000):
        sum1 += 1 / i
        count += 1
        if sum1 > 4:
            return count


print(calc())