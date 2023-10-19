dict1 = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят':50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90, 'сто': 100}
vvod = list(input().split(' '))
z = None
def res(res):
    print(res)
    dict2 = dict(zip(dict1.values(), dict1.keys()))
    print(dict2)
    a = dict2.get(res)
    print(a)

def length3():
    a = vvod[0]
    b = vvod[1]
    c = vvod[2]
    x = dict1.get(a)
    y = dict1.get(c)
    if b == 'плюс':
        res = x + y
    elif b == 'минус':
        res = x - y
    elif b == 'умножить':
        res = x * y
    else:
        print('неверный ввод')
    return res
def length4():
    a = vvod[0]
    b = vvod[1]
    c = vvod[2]
    d = vvod[3]
    x = dict1.get(a)
    y = dict1.get(b)
    z = dict1.get(c)
    m = dict1.get(d)
    if y == None and z != None:
        v = z + m
        if b == 'плюс':
            res = x + v
        elif b == 'минус':
            res = x - v
        elif b == 'умножить':
            res = x * v
        else:
            print('неверный ввод')
    elif z == None and y != None:
        v = x + y
        if c == 'плюс':
            res = v + m
        elif c == 'минус':
                res = v - m
        elif c == 'умножить':
                res = v * m
        else:
            print('неверный ввод')
    elif y == None and z == None:
        res = x * m
    else:
        print('неверный ввод')
    return res

def length5():
    a = vvod[0]
    b = vvod[1]
    c = vvod[2]
    d = vvod[3]
    e = vvod[4]
    x = dict1.get(a)
    y = dict1.get(b)
    z = dict1.get(c)
    m = dict1.get(d)
    n = dict1.get(e)
    if x != None and y != None and z == None and m != None and n != None:
        if c == 'плюс':
            v = x + y
            l = m + n
            res = v + l
        elif c == 'минус':
            v = x + y
            l = m + n
            res = v - l
    elif x != None and y == None and z == None and m != None and n != None:
        v = m + n
        res = x * v
    elif x != None and y != None and z == None and m == None and n != None:
        v = x + y
        res = v * n
    else:
        print('неверный ввод')
    return res

def length6():
    a = vvod[0]
    b = vvod[1]
    c = vvod[2]
    d = vvod[3]
    e = vvod[4]
    f = vvod[5]
    x = dict1.get(a)
    y = dict1.get(b)
    z = dict1.get(c)
    m = dict1.get(d)
    n = dict1.get(e)
    l = dict1.get(f)
    print(x ,y, z, m, n, l)
    r = x + y
    t = n + l
    if z == None and m == None:
        res = r * t
    else:
        print('неверный ввод')
    return res

if len(vvod) == 3:
    length3()
elif len(vvod) == 4:
    length4()
elif len(vvod) == 5:
    length5()
elif len(vvod) == 6:
    length6()
else:
    print('неверный ввод')