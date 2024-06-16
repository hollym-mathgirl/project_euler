test_num = 10000

def sum_of_divisors(limit):
    sum_pairs = {}
    for num in range(1, limit + 1):
        divisors = [i for i in range(1, num) if num % i == 0]
        sum_pairs[num] = sum(divisors)
    return sum_pairs
        
def check_for_amicable(sum_pairs):
    amicables = []
    for number, divisor_sum in sum_pairs.items():
        if divisor_sum != number and divisor_sum in sum_pairs and sum_pairs[divisor_sum] == number:
            amicables.append(number)
    return sum(amicables)

sum_pairs = sum_of_divisors(test_num)
print(check_for_amicable(sum_pairs))
