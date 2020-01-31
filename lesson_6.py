# --------ТЕСТИРОВАНИЕ ФУНКЦИЙ--------

# проверка на простоту
def is_prime(n):
    i = 2
    while n > i:
        if n % i == 0:
            break
        i += 1
    return i == n
print(is_prime(n))

def test_is_prime_1():
    assert is_prime_1(7)  == True

def test_is_prime_2():
    assert is_prime_2(344) == False

# выводит список всех делителей числа;
def all_dividers(n):
    result = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            result.append(i)
        else:
            i += 1
    if  n > 1:
        result.append(n)
    return result
print(all_dividers(24))

def test_all_dividers_1():
    assert all_dividers_1(7) == 7

# выводит самый большой простой делитель числа.
def greatest_pr_div(n):
    prime_num = all_dividers(n)
    max_num = 0
    for i in prime_num:
        if i > max_num:
            max_num = i
    return(max_num)
print(greatest_pr_div(23244))

def test_greatest_pr_div():
    assert greatest_pr_div(149) == 149
    assert greatest_pr_div(-149) == 0