import random

# Константи
H = 1  # голова, герб та її величина
T = -1  # Хвіст, номінал та ЇЇ величина
J = 4  # Кількість повторів. Загалом я буду намагатися робити код більш гнучким щодо зміни констант
M = 0
N = 1000_000

all_vars = 2**J


def get_ksi(h) -> int:
    '''
    Нам всі значення ксі легко отримати за простою формулою,
     яка залежить виключно від кількості випавших гербів
    :param h:
    :return: int
    '''
    return h * H + T * (J - h)


def bf_variants() -> dict:
    variants = {}  # Словник вв в брутфорсі. ключем буде комбінація H та T
    for j in range(2 ** J):
        binj = bin(j)
        ksi = get_ksi(binj.count('1'))  # Я геній. найпростіший сопсіб
        # Перебрати всі варіанти

        variants[bin(j)[2:].zfill(J)] = ksi

    return variants

def simul_variants(n) -> dict:
    '''
    Загалом краще було б збрерігати {комбінація: кільскість повторів}
    Щоб фактично повністю приблало обмеження по пом'яті для кількості симуляцій,
    але навіть так має вистачити на 10_000_000+ симуляцій
    :param n:
    :return:
    '''
    variants = {}
    for j in range(n):
        binj = bin(random.randint(0, (2**J-1)))
        ksi = get_ksi(binj.count('1'))  # Я геній. найпростіший сопсіб
        # Перебрати всі варіанти

        variants[j] = ksi

    return variants


def distribution_fun(variants: bf_variants()) -> dict:
    disfun = {}
    for value in variants.values():
        v = int(value)
        disfun[v] = disfun.get(v, 0) + 1

    return disfun


def display_disfun(disfun: distribution_fun()):
    for key, val in disfun.items():
        print(f"{key}      {val}/{all_vars}      {val / all_vars}")


def p_from(m, disfun: distribution_fun()):
    return disfun[m] / all_vars


def e_math(disfun: distribution_fun(), k = 1) -> float:
    e = 0
    for key, val in disfun.items():
        e += key**k * val / all_vars
    return e

def var(disfun: distribution_fun(), e: e_math()) -> float:
    ee = e ** 2
    e_dksi = e_math(disfun, 2)
    return e_dksi - ee


# d = distribution_fun(bf_variants())
# print(d)
# display_disfun(d)
#
# print(p_from(M, d))
# print(var())


all_vars = N
s = simul_variants(N)
d_s = distribution_fun(s)
display_disfun(d_s)