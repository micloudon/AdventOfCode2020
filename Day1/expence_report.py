from entries import entries

# find 2 values from entries that equal 2020 and multiply them
# all values need to be compared against each other to see they equal 2020

# brute force solution
# Time complexity O(n^2)
def expenceReportBf(entries):
    sm = 2020
    for i in entries:
        for k in entries:
            if i + k == sm:
                return i *  k

print(expenceReportBf(entries))


# More efficient memoized solution
# time complexity O(n log n)
def expenceReportM(entries):
    sm = 2020

    remainders = []

    for i in entries:
        remainders.append(sm - i)

    for k in entries:
        if k in remainders:
            return k * (sm - k)

print(expenceReportM(entries))



