try:
    sum1 = 0
    count = 0
    for i in range(0, 1000):
        sum1 += 1 / i
        count += 1
        if sum1 > 4:
            print(count)
            break
except ZeroDivisionError as e:
    print(e)

finally:
    print("------")
    sum1 = 0
    count = 0
    for i in range(1, 1000):
        sum1 += 1 / i
        count += 1
        if sum1 > 4:
            print(count)
            break