# Every line of input is bag
# Bags must be checked to see if they can contain Shiny Gold Bags 
# Bag can contain other bags
# How many bags can contain the Shiny Gold bag

# Example
# Red bag contains Shiny Gold bag
# blue bag contains red bag
# green bag contains blue
# Shiny gold bag contain white bag
# 3 bags contain the Shiny Gold bag
# This problem is difficult to understand and explain, please refer to the README file for further instructions

bags = open('day7.input')

shinyGold = []
shinyGold2 = []
shinyGold21 = []
shinyGold3 = []
shinyGold31 = []
shinyGold4 = []
shinyGold41 = []
shinyGold5 = []
shinyGold51 = []
shinyGold6 = []
shinyGold61 = []
shinyGold7 = []
shinyGold71 = []
shinyGold8 = []
shinyGold81 = []
shinyGold9 = []
shinyGold91 = []
b = []

for line in bags:
    b.append(line)
    if 'shiny gold bag' in line:
        line2 = line.split(' contain')
        line3 = line2[0]
        shinyGold.append(line3[:-5])

# check first iteration with whole list
for index in b:
    for j in shinyGold:
        if j in index:
            shinyGold2.append(index)


for x in shinyGold2:
    x2 = x.split(' contain')
    x3 = x2[0]
    shinyGold21.append(x3[:-5])


# check 2nd iteration with whole list
for index2 in b:
    for j2 in shinyGold21:
        if j2 in index2:
            shinyGold3.append(index2)

for y in shinyGold3:
    y2 = y.split(' contain')
    y3 = y2[0]
    shinyGold31.append(y3[:-5])

# # check 3rd iteration with whole list
for index3 in b:
    for j3 in shinyGold31:
        if j3 in index3:
            shinyGold4.append(index3)

for z in shinyGold4:
    z2 = z.split(' contain')
    z3 = z2[0]
    shinyGold41.append(z3[:-5])

# check 4th iteration with whole list
for index4 in b:
    for j4 in shinyGold41:
        if j4 in index4:
            shinyGold5.append(index4)

for w in shinyGold5:
    w2 = w.split(' contain')
    w3 = w2[0]
    shinyGold51.append(w3[:-5])

# check 5th iteration with whole list
for index5 in b:
    for j5 in shinyGold51:
        if j5 in index5:
            shinyGold6.append(index5)

for k in shinyGold6:
    k2 = k.split(' contain')
    k3 = k2[0]
    shinyGold61.append(k3[:-5])

# check 6th iteration with whole list
for index6 in b:
    for j6 in shinyGold61:
        if j6 in index6:
            shinyGold7.append(index6)

for v in shinyGold7:
    v2 = v.split(' contain')
    v3 = v2[0]
    shinyGold71.append(v3[:-5])

# check 7th iteration with whole list
for index7 in b:
    for j7 in shinyGold71:
        if j7 in index7:
            shinyGold8.append(index7)

for f in shinyGold8:
    f2 = f.split(' contain')
    f3 = f2[0]
    shinyGold81.append(f3[:-5])

# check 8th iteration with whole list
for index8 in b:
    for j8 in shinyGold81:
        if j8 in index8:
            shinyGold9.append(index8)

for q in shinyGold9:
    q2 = q.split(' contain')
    q3 = q2[0]
    shinyGold91.append(q3[:-5])


# check one more iteration to see if len matchs
# if it does, no more checks are needed
# check 9th iteration with whole list
# for index9 in b:
#     for j9 in shinyGold91:
#         if j9 in index9:
#             shinyGold10.append(index9)

# for c in shinyGold10:
#     c2 = c.split(' contain')
#     c3 = c2[0]
#     shinyGold101.append(c3[:-5])

shinyGold92 = list(dict.fromkeys(shinyGold91))

print(len(shinyGold92)-1)

