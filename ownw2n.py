# тут происходит перевод из числа в слово
import decimal

units = (
    u'ноль',
    (u'один', u'одна'),
    (u'два', u'две'),
    u'три', u'четыре', u'пять',
    u'шесть', u'семь', u'восемь', u'девять'
)

teens = (
    u'десять', u'одиннадцать',
    u'двенадцать', u'тринадцать',
    u'четырнадцать', u'пятнадцать',
    u'шестнадцать', u'семнадцать',
    u'восемнадцать', u'девятнадцать'
)

tens = (
    teens,
    u'двадцать', u'тридцать',
    u'сорок', u'пятьдесят',
    u'шестьдесят', u'семьдесят',
    u'восемьдесят', u'девяносто'
)

hundreds = (
    u'сто', u'двести',
    u'триста', u'четыреста',
    u'пятьсот', u'шестьсот',
    u'семьсот', u'восемьсот',
    u'девятьсот'
)

orders = (# множественные числа
    ((u'тысяча', u'тысячи', u'тысяч'), 'f'),
    ((u'миллион', u'миллиона', u'миллионов'), 'm'),
    ((u'миллиард', u'миллиарда', u'миллиардов'), 'm'),
)

minus = u'минус'


def thousand(rest, sex):
    prev = 0
    plural = 2
    name = []
    use_teens = rest % 100 >= 10 and rest % 100 <= 19
    if not use_teens:
        data = ((units, 10), (tens, 100), (hundreds, 1000))
    else:
        data = ((teens, 10), (hundreds, 1000))
    for names, x in data:
        cur = int(((rest - prev) % x) * 10 / x)
        prev = rest % x
        if x == 10 and use_teens:
            plural = 2
            name.append(teens[cur])
        elif cur == 0:
            continue
        elif x == 10:
            name_ = names[cur]
            if isinstance(name_, tuple):
                name_ = name_[0 if sex == 'm' else 1]
            name.append(name_)
            if cur >= 2 and cur <= 4:
                plural = 1
            elif cur == 1:
                plural = 0
            else:
                plural = 2
        else:
            name.append(names[cur-1])
    return plural, name


def num2text(num, main_units=((u'', u'', u''), 'm')):
    _orders = (main_units,) + orders
    if num == 0:
        return ' '.join((units[0], _orders[0][0][2])).strip() # ноль

    rest = abs(num)
    ord = 0
    name = []
    while rest > 0:
        plural, nme = thousand(rest % 1000, _orders[ord][1])
        if nme or ord == 0:
            name.append(_orders[ord][0][plural])
        name += nme
        rest = int(rest / 1000)
        ord += 1
    if num < 0:
        name.append(minus)
    name.reverse()
    return ' '.join(name).strip()


def decimal2text(value, places=2,
                 int_units=(('', '', ''), 'm'),
                 exp_units=(('', '', ''), 'm')):
    value = decimal.Decimal(value)
    q = decimal.Decimal(10) ** -places

    integral, exp = str(value.quantize(q)).split('.')
    return u'{} {}'.format(
        num2text(int(integral), int_units),
        num2text(int(exp), exp_units))

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        try:
            num = sys.argv[1]
            if '.' in num:
                print(decimal2text(decimal.Decimal(num)))
            else:
                print(num2text(int(num)))
        except ValueError:
            print (sys.stderr, "Invalid argument {}".format(sys.argv[1]))
        sys.exit()

# тут происходит перевод из слов в число
number_system = {
    'ноль': 0,
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
    'сто': 100,
}

decimal_words = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']

def number_formation(number_words):
    numbers = []
    for number_word in number_words:
        numbers.append(number_system[number_word])
    if len(numbers) == 4:
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
    elif len(numbers) == 3:
        return numbers[0] * numbers[1] + numbers[2]
    elif len(numbers) == 2:
        if 100 in numbers:
            return numbers[0] * numbers[1]
        else:
            return numbers[0] + numbers[1]
    else:
        return numbers[0]

def get_decimal_sum(decimal_digit_words):
    decimal_number_str = []
    for dec_word in decimal_digit_words:
        if(dec_word not in decimal_words):
            return 0
        else:
            decimal_number_str.append(number_system[dec_word])
    final_decimal_string = '0.' + ''.join(map(str,decimal_number_str))
    return float(final_decimal_string)

def word_to_num(number_sentence):
    if type(number_sentence) is not str:
        raise ValueError("Ввод не есть строка!")

    number_sentence = number_sentence.replace('-', ' ')
    number_sentence = number_sentence.lower()

    if(number_sentence.isdigit()):
        return int(number_sentence)

    split_words = number_sentence.strip().split()

    clean_numbers = []
    clean_decimal_numbers = []

    for word in split_words:
        if word in number_system:
            clean_numbers.append(word)

    # чек ошибочного ввода
    if len(clean_numbers) == 0:
        raise ValueError("Неправильный ввод") 

    if clean_numbers.count('thousand') > 1 or clean_numbers.count('million') > 1 or clean_numbers.count('billion') > 1 or clean_numbers.count('point')> 1:
        raise ValueError("Неправильный ввод")

    if clean_numbers.count('point') == 1:
        clean_decimal_numbers = clean_numbers[clean_numbers.index('point')+1:]
        clean_numbers = clean_numbers[:clean_numbers.index('point')]

    billion_index = clean_numbers.index('billion') if 'billion' in clean_numbers else -1
    million_index = clean_numbers.index('million') if 'million' in clean_numbers else -1
    thousand_index = clean_numbers.index('thousand') if 'thousand' in clean_numbers else -1

    if (thousand_index > -1 and (thousand_index < million_index or thousand_index < billion_index)) or (million_index>-1 and million_index < billion_index):
        raise ValueError("Неправильный ввод")

    total_sum = 0

    if len(clean_numbers) > 0:
        if len(clean_numbers) == 1:
                total_sum += number_system[clean_numbers[0]]

        else:
            if billion_index > -1:
                billion_multiplier = number_formation(clean_numbers[0:billion_index])
                total_sum += billion_multiplier * 1000000000

            if million_index > -1:
                if billion_index > -1:
                    million_multiplier = number_formation(clean_numbers[billion_index+1:million_index])
                else:
                    million_multiplier = number_formation(clean_numbers[0:million_index])
                total_sum += million_multiplier * 1000000

            if thousand_index > -1:
                if million_index > -1:
                    thousand_multiplier = number_formation(clean_numbers[million_index+1:thousand_index])
                elif billion_index > -1 and million_index == -1:
                    thousand_multiplier = number_formation(clean_numbers[billion_index+1:thousand_index])
                else:
                    thousand_multiplier = number_formation(clean_numbers[0:thousand_index])
                total_sum += thousand_multiplier * 1000

            if thousand_index > -1 and thousand_index != len(clean_numbers)-1:
                hundreds = number_formation(clean_numbers[thousand_index+1:])
            elif million_index > -1 and million_index != len(clean_numbers)-1:
                hundreds = number_formation(clean_numbers[million_index+1:])
            elif billion_index > -1 and billion_index != len(clean_numbers)-1:
                hundreds = number_formation(clean_numbers[billion_index+1:])
            elif thousand_index == -1 and million_index == -1 and billion_index == -1:
                hundreds = number_formation(clean_numbers)
            else:
                hundreds = 0
            total_sum += hundreds
    if len(clean_decimal_numbers) > 0:
        decimal_sum = get_decimal_sum(clean_decimal_numbers)
        total_sum += decimal_sum

    return total_sum

s=input().split()
print(s)

for i in range(len(s)-1):
    if s[i]=='плюс':
        s[i]='+'
    elif s[i]=='минус':
        s[i]='-'
    elif s[i]=='умножить' and s[i+1]=='на':
        s[i]='*'
        del s[i+1]
    elif s[i]=='поделить' and s[i+1]=='на':
        s[i]='/'
        del s[i+1]
    elif s[i]=='скобка' and s[i+1]=='открывается':
        s[i]='('
    elif s[i]=='скобка' and s[i+1]=='закрывается':
        s[i]=')'
    elif s[i]!='*' and s[i]!='+' and s[i]!='-' and s[i]!='/' and s[i]!='(' and s[i]!=')' and s[i]!='закрывается' and s[i]!='открывается':
        s[i]=word_to_num(s[i])
    else:
        continue

n=len(s)
if not(str(s[n-1]).isnumeric()) and s[n-1]!='закрывается' and s[n-1]!='открывается':
    s[n-1]=word_to_num(s[n-1])
elif s[n-1]=='закрывается':
    del s[i]
b=len(s)


for i in range(len(s)-1): 
    if str(s[i]).isnumeric() and str(s[i+1]).isnumeric():
        s[i]+=s[i+1]
        s[i+1]=''

for i in range(len(s)):
    if s[i]=='открывается' or s[i]=='закрывается':
        s[i]=''

new_s=''
for i in range(len(s)):
    new_s+=str(s[i])
print(new_s)
print(num2text(eval(new_s)))