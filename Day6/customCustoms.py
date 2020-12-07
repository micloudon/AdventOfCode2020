# count the number of unique occurrences in eack valueset

# abc = 3

# a
# b = 3
# c

# ab 
# ac = 3

# a
# a = 1
# a
# a

# b = 1

# format the dataset into list items
customs = open('day6.input')
customs2 = " ".join(line.strip() for line in customs) 
customs3 = customs2.replace("  ", '\n')
l = customs3.splitlines()

l2 = []

# remove spaces and duplicates
for i in l:
    line = ''.join(set(i))
    line2 = line.replace(' ', '')
    l2.append(line2)

count = 0

for j in l2:
    count += len(j)

print(count)