# '#' are trees and '.' are open land
# I need to tranverse the input in multiple ways: 
# Right 1, down 1
# Right 3, down 1
# Right 5, down 1
# Right 7, down 1
# Right 1, down 2
# I need to count how many trees I encounter transersing the whole slope and multiply them together
# I have to duplicate the input horizonally so I don't fall off the edge

import numpy as np
arr = []
l = 0

# Here I turn the input into a matrix (not a true matrix, really a list of lists)
# I cut out the \n characters and count the number of lines
slope = open('day3.input')
slope = [line[:-1] for line in slope]
for line in slope:
    l += 1
    for i in line:
        arr.append(i)


matrix = np.array_split(arr, l)    


# now I tranverse the matrix as specified above
# I use an if statment to keep the pointer inbounds and to simulate an infinite horizonatal input
# I check for trees and count the trees 



# all these for loops and variable can get a bit repeative and unrully, but I'll keep them here for demonstration purposes
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
count = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

# 80, 
for i in matrix[1:]:
    c1 += 1
    if c1 >= 31:
        c1 = c1 - 31
    if i[c1] == "#":
        count += 1

for i in matrix[1:]:
    c2 += 3
    if c2 >= 31:
        c2 = c2 - 31
    if i[c2] == "#":
        count2 += 1


for i in matrix[1:]:
    c3 += 5
    if c3 >= 31:
        c3 = c3 - 31
    if i[c3] == "#":
        count3 += 1

for i in matrix[1:]:
    c4 += 7
    if c4 >= 31:
        c4 = c4 - 31
    if i[c4] == "#":
        count4 += 1


for i in matrix[2::2]:
    c5 += 1
    if c5 >= 31:
        c5 = c5 - 31
    if i[c5] == "#":
        count5 += 1



print(count, count2, count3, count4, count5)
print(count * count2 * count3 * count4 * count5)