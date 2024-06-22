#create a list to populate
terms = []
#nested for loops covering the terms in the problem
for a in range(2, 101):
    for b in range(2, 101):
#append the terms to the list
        terms.append(a**b)
        terms.append(b**a)
#make a set so only distinct items will count
distinct = set(terms)
print(len(distinct))
