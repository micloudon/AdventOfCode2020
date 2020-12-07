# count the number of values that repeat through each line of data

# abc = 3

# a
# b = 0
# c

# ab 
# ac = 1

# a
# a = 1
# a
# a

# b = 1

# brlmq
# tbrq = 3
# qrbx

from collections import Counter

# format the dataset into list items
customs = open('day6.input')
customs2 = " ".join(line.strip() for line in customs) 
customs3 = customs2.replace("  ", '\n')
l = customs3.splitlines()

l2 = []

# compare occurrence of repeating values to space in element
for i in l:
    spaces = i.count(" ")
    elements = Counter(i)
    m = [k for k,v in elements.items() if v> spaces]
    l2.append(m)


count = 0

for j in l2:
    count += len(j)

print(count)

    



