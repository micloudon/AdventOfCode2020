# '#' are trees and '.' are open land
# I need to tranverse the input, moving down 1 and 3 to rhe right
# I need to count how many trees I encounter transersing the whole slope
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

x = 0
count = 0

for i in matrix[1:]:
    x += 3
    if x >= 31:
        x = x - 31
    if i[x] == "#":
        count += 1


print(count)

