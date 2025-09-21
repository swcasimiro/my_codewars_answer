# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
def accum(st):
    st, text = list(st), ""

    for i in range(len(st)): text += st[i] * (i + 1) + "-"

    text = text[:-1]
    st, text = text.split('-'), ""

    for i in st: text += i.title() + '-'

    return text[:-1]


# https://www.codewars.com/kata/596343a24489a8b2a00000a2
def is_it_a_num(s: str) -> str:
    phone = ''.join(c if c.isdigit() else ' ' for c in s).split()
    phone = "".join(phone)

    if phone[0:1] == "0" and len(phone) == 11:
        return phone

    return "Not a phone number"


# https://www.codewars.com/kata/59727ff285281a44e3000011
def band_name_generator(name):
    if name[0] == name[-1]: return f"{name[0].upper()}{name[1:]}{name[1:]}"
    return f"The {name[0].upper()}{name[1:]}"


# https://www.codewars.com/kata/63f96036b15a210058300ca9
def second_symbol(s, symbol):
    lst, point = list(s), 0

    for i in range(len(lst)):
        if lst[i] == symbol:
            point += 1

        elif point == 2:
            return i - 1

    return -1


# https://www.codewars.com/kata/5299413901337c637e000004
def get_missing_element(seq):
    seq = sorted(seq)

    for i in range(len(seq)):
        if i != seq[i]:
            return i

    else:
        return i + 1


# https://www.codewars.com/kata/59a96d71dbe3b06c0200009c
def generate_shape(n):
    lst = []
    for i in range(n): lst.append('+'*n)
    return "\n".join(lst)


# https://www.codewars.com/kata/558fc85d8fd1938afb000014
def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    lst = []

    i = 0
    while len(lst) < 2:
        if numbers[i] >= 0:
            lst.append(numbers[i])
        i += 1

    return sum(lst)


# https://www.codewars.com/kata/56a921fa8c5167d8e7000053
def password(st):
    psw_upper = 0
    lst = list(st)
    for i in range(len(lst)):
        if lst[i].isupper():
            psw_upper = 1

    if psw_upper != 1:
        return False

    psw_lower = 0

    for i in range(len(lst)):
        if lst[i].islower():
            psw_lower = 1

    psw_num = 0

    for i in range(len(lst)):
        if lst[i] in '1234567890':
            psw_num = 1

    psw_len = 0

    if len(lst) > 7:
        psw_len = 1

    if psw_upper == 1 and psw_lower == 1 and psw_num == 1 and psw_len == 1:
        return True

    return False



# https://www.codewars.com/kata/5a6d3bd238f80014a2000187
def owned_cat_and_dog(cat_years, dog_years):
    # funny if ahahaha
    c_num = 0

    if cat_years > 14:
        c_num = 1

        if cat_years > 23:
            c_num = 2

    d_num = 0

    if dog_years > 14:
        d_num = 1

        if dog_years > 23:
            d_num = 2

    if dog_years >= 29:
        dog_years -= 24
        while dog_years >= 5:
            dog_years -= 5
            d_num += 1

    if cat_years >= 28:
        cat_years -= 24
        while cat_years >= 4:
            cat_years -= 4
            c_num += 1

    return [c_num, d_num]


# https://www.codewars.com/kata/57ed4cef7b45ef8774000014
def boredom(staff):
    data = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }

    num = 0

    for i in staff:
        if staff[i] in data:
            value = staff[i]
            num += data[value]

    if num <= 80: return 'kill me now'
    if num > 80 and num < 100: return 'i can handle this'

    return 'party time!!'


# https://www.codewars.com/kata/5ae7e3f068e6445bc8000046
def next_happy_year(year):
    year += 1

    for i in range(100):
        lst = set(list(str(year)))

        if len(lst) == len(str(year)):
            return year

        year += 1


# https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1
def capitalize(s, ind):
    lst = list(s)

    for i in ind:
        if len(lst) >= i:
            lst[i] = lst[i].upper()

    return "".join(lst)


# https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce
def no_odds(values):
    lst = []

    for i in values:
        if i % 2 == 0:
            lst.append(i)

    return lst


# https://www.codewars.com/kata/5983cba828b2f1fd55000114
def odd_one(arr):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            return i

    return -1