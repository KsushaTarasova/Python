def func(arg):
    t = str(type(arg))

    if t == "<class 'list'>":
        temp = 0
        arg = list(set(arg))
        for i in range(len(arg)):
            if arg[i] > 0:
                temp = i
                break
        sum1 = 0
        for i in range(temp, len(arg)):
            sum1 += arg[i]
        return sum1

    elif t == "<class 'dict'>":
        arg1 = sorted(arg, key=arg.get)
        arg2 = reversed(arg1)
        for i in arg2:
            print(f"{i}: {arg[i]}")

    elif t == "<class 'int'>":
        count = 0
        for i in range(2, arg // 2):
            if arg % i == 0:
                count = 1
        if count == 1:
            print("Число составное")
        else:
            print("Число простое")

    elif t == "<class 'str'>":
        for i in range(len(arg)):
            print(ord(arg[i]))


print("Список:")
my_list = [-3, 0, -7, 4, 5, -4, 7, -3, 5, 4]
print(func(my_list))
print("Словарь:")
my_dict = {1: 47, 2: 84, 3: 97, 4: 1, 5: -8, 6: 100}
print(func(my_dict))
print("Число:")
c = 5
print(func(c))
c = 10
print(func(c))
print("Строка:")
s = "Привет!"
print(func(s))