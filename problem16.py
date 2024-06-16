value = 1000
answer = 2**value
string = str(answer)

sum = 0

for digit in string:
    sum += int(digit)

print(sum)
