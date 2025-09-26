
# https://www.codewars.com/kata/58bf9bd943fadb2a980000a7
def who_is_paying(name):
    lst = []

    if len(name) > 2:
        lst = [name, name[0] + name[1]]
        return lst

    if len(name) < 3:
        return [name]


# https://www.codewars.com/kata/5583090cbe83f4fd8c000051
def digitize(n):
    n, lst = str(n)[::-1], []
    for i in range(len(n)): lst.append(int(n[i]))
    return lst


# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2
def remove_every_other(my_list):
    lst = []
    for i in range(len(my_list)):
        if i == 0 or i % 2 == 0: lst.append(my_list[i])
    return lst


# https://www.codewars.com/kata/583710ccaa6717322c000105
def simple_multiplication(number) :
    return (8*number)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8)-(number*8)+ (number*8) if number % 2 == 0 else 9*number


# https://www.codewars.com/kata/57f780909f7e8e3183000078
def grow(arr):
    res = 1
    for i in range(len(arr)):
        res *= arr[i]

    return res


# https://www.codewars.com/kata/53ee5429ba190077850011d4
def double_integer(i):
    return i*2


# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
def count_sheep(n):
    lst = []
    for i in range(0, n):
        lst.append(f"{i + 1} sheep...")

    return "".join(lst)


# https://www.codewars.com/kata/57e3f79c9cb119374600046b
def hello(name=False):
    return f'Hello, {name.capitalize()}!' if name else 'Hello, World!'


# https://www.codewars.com/kata/551b4501ac0447318f0009cd
def boolean_to_string(b):
    return "True" if b == True else "False"


# https://www.codewars.com/kata/57a386117cb1f31890000039
def parse_float(string):
    try:
        return float(string)

    except(ValueError, TypeError):
        return None


# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce
def multi_table(number):
    lst = []
    value = ''
    for i in range(10):
        value = f"{i+1} * {number} = {(i+1) * number}"
        lst.append(value)
    return "\n".join(lst)


# https://www.codewars.com/kata/55c28f7304e3eaebef0000da
def create_array(n):
    res = []
    for i in range(n):
        res.append(i + 1)

    return res


# https://www.codewars.com/kata/5963c18ecb97be020b0000a2
def derive(coefficient, exponent):
    return f"{coefficient * exponent}x^{exponent-1}"


# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed
def replace_exclamation(st):
    lst = list(st)

    for i in range(len(lst)):
        if lst[i] in 'aeiouAEIOU':
            lst[i] = '!'

    return "".join(lst)


# https://www.codewars.com/kata/55c90cad4b0fe31a7200001f
def build_string(*args):
    return "I like {}!".format(", ".join(args))


# https://www.codewars.com/kata/57ec8bd8f670e9a47a000f89
def mouth_size(animal):
    return "small" if animal.lower() == "alligator" else "wide"


# https://www.codewars.com/kata/559ac78160f0be07c200005a
def name_shuffler(str_):
    return " ".join(str_.split()[::-1])


# https://www.codewars.com/kata/559ac78160f0be07c200005a
def playerRankUp(pts):
    return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." if pts >= 100 else False


# https://www.codewars.com/kata/5265326f5fda8eb1160004c8
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⢀⣴⠟⠉⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣀⢀⣾⠿⠻⢶⣄⠀⠀⣠⣶⡿⠶⣄⣠⣾⣿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢻⣿⣿⡿⣿⠿⣿⡿⢼⣿⣿⡿⣿⣎⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠉⠛⢛⣛⡉⠀⠀⠙⠛⠻⠛⠑⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣧⣤⣴⠿⠿⣷⣤⡤⠴⠖⠳⣄⣀⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣀⣟⠻⢦⣀⡀⠀⠀⠀⠀⣀⡈⠻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠉⡇⠀⠀⠛⠛⠛⠋⠉⠉⠀⠀⠀⠹⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠀⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠈⠑⠪⠷⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣦⣼⠛⢦⣤⣄⡀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠢⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠲⠖⠛⠻⣿⡿⠛⠉⠉⠻⠷⣦⣽⠿⠿⠒⠚⠋⠉⠁⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢀⣾⠛⠁⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⠀
# ⠀⠀⠀⠀⣰⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀
# ⠀⠀⠀⣰⣿⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣧⣄⠀⠀⠀⠀⠀⠀⢳⡀⠀
# ⠀⠀⠀⣿⡾⢿⣀⢀⣀⣦⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⣫⣿⡿⠟⠻⠶⠀⠀⠀⠀⠀⢳⠀
# ⠀⠀⢀⣿⣧⡾⣿⣿⣿⣿⣿⡷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢿⣿⣧⠀⡀⠀⢀⣀⣀⢒⣤⣶⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
# ⠀⠀⡾⠁⠙⣿⡈⠉⠙⣿⣿⣷⣬⡛⢿⣶⣶⣴⣶⣶⣶⣤⣤⠤⠾⣿⣿⣿⡿⠿⣿⠿⢿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
# ⠀⣸⠃⠀⠀⢸⠃⠀⠀⢸⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⠟⡉⠀⠀⠀⠈⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
# ⠀⣿⠀⠀⢀⡏⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠉⠠⠿⠟⠻⠟⠋⠉⢿⣿⣦⡀⢰⡀⠀⠀⠀⠀⠀⠀⠁
# ⢀⣿⡆⢀⡾⠀⠀⠀⠀⣾⠏⢿⣿⣿⣿⣯⣙⢷⡄⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣻⢿⣷⣀⣷⣄⠀⠀⠀⠀⢸⠀
# ⢸⠃⠠⣼⠃⠀⠀⣠⣾⡟⠀⠈⢿⣿⡿⠿⣿⣿⡿⠿⠿⠿⠷⣄⠈⠿⠛⠻⠶⢶⣄⣀⣀⡠⠈⢛⡿⠃⠈⢿⣿⣿⡿⠀⠀⠀⠀⠀⡀
# ⠟⠀⠀⢻⣶⣶⣾⣿⡟⠁⠀⠀⢸⣿⢅⠀⠈⣿⡇⠀⠀⠀⠀⠀⣷⠂⠀⠀⠀⠀⠐⠋⠉⠉⠀⢸⠁⠀⠀⠀⢻⣿⠛⠀⠀⠀⠀⢀⠇
# ⠀⠀⠀⠀⠹⣿⣿⠋⠀⠀⠀⠀⢸⣧⠀⠰⡀⢸⣷⣤⣤⡄⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⢼⡇
# ⠀⠀⠀⠀⠀⠙⢻⠄⠀⠀⠀⠀⣿⠉⠀⠀⠈⠓⢯⡉⠉⠉⢱⣶⠏⠙⠛⠚⠁⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⡇
# ⠀⠀⠀⠀⠀⠀⠻⠄⠀⠀⠀⢀⣿⠀⢠⡄⠀⠀⠀⣁⠁⡀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⢀⣐⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢠⡇

def number_to_string(num):
    return str(num)
