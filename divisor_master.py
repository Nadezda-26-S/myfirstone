
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
if __name__ == '__lesson_5':

def is_prime(n):
    while n > 1:
        for n % i == 0:
            i += 1
    return n
print(is_prime(n))

# 2) выводит список всех делителей числа;

def all_dividers(n):
    result = []
    while i * i <= n:
        if n % i == 0:
            n //= i
            result.append(i)
        else:
            i += 1
    if  n > 1:
        result.append(n)
    return result
print(all_dividers(n))

# 3) выводит самый большой простой делитель числа.

def greatest_pr_div(n):
    max = []
    for n % i == 0:
        if max < max_temp[i]:
            max = max_temp[i]
print(max)

# КАК ЧЕРЕЗ ЛЯМБДУ:: greatest_pr_div() = lambda n: greatest_pr_div(i) > greatest_pr_div(i+1) if n > 1 else &
# if ... lambda n, i: i if i>(i+1) else i+1
