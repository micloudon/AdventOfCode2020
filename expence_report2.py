from entries import entries
import numpy 

# find 3 values from entries that equal 2020 and multiply them
# all values need to be compared against each other to see they equal 2020

# Brute Force solution
# time complexity O(n^3)
def expenceReportBf(entries):
    sm = 2020

    for i in entries:
        for k in entries:
             for j in entries:
                if i + k + j == sm:
                    return i * k * j

print(expenceReportBf(entries))


# Memoized solution
# Time complexity O(n^2)
def expenceReportM(entries):
    sm = 2020
    remainders = []
    values = []

    for i in entries:
        for j in entries:
            remainders.append(sm - i - j)

    for k in entries:
        if k in remainders:
            values.append(k)

    return numpy.prod(values)


print(expenceReportM(entries))



        
