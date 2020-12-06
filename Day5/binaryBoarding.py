# seat id = (row * 8) + column
# row, columnn need to found
# the first 7 chars determine the row out of 128rows 0-127
# the last 3 chars determine the column out of 8 columns 0-7
# every boarding pass is 10 char long

# Check README for more instructions 

boardingPass = open('day5.input')

row = 0
column = 0


# I make some searchs to find to boarding pass the highest value
# After some expermentation I use this search pattern to find the boarding pass with the highest value
for i in boardingPass:
    if i[0] == "B":
        if i[1] == "B":
            if i[2] == 'F':
                if i[3] == 'B':
                    if i[4] == 'B':
                        print(i)




# Row 
# 64 - 127
# 96 - 127
# 96 - 111
# 104 - 111
# 108 - 111
# 108 - 109
# 108

# Columns
# 0 - 3
# 0 - 1
# 0

