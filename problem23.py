def sum_of_divisors(limit):
    sum_pairs = {}
    for num in range(1, limit + 1):
        divisors = [i for i in range(1, (num // 2) + 1) if num % i == 0]
        sum_pairs[num] = sum(divisors)
    return sum_pairs

a = sum_of_divisors(28123)

def check_for_abundant_addends(sum_pairs):
    abundant = [number for number, divisor_sum in sum_pairs.items() if divisor_sum > number]
    return abundant

b = check_for_abundant_addends(a)

def check_for_problem(abundant):
    possible_sums = set()
    abundant_len = len(abundant)
    for i in range(abundant_len):
        for j in range (i, abundant_len):
            possible_sum = abundant[i] + abundant[j]
            if possible_sum <= 28123:
                possible_sums.add(abundant[i] + abundant[j])
    return possible_sums

c = check_for_problem(b)

addends = [i for i in range (1, 28124) if i not in c]
print(sum(addends))
