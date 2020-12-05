# Input must be seperated into different entries
# I have to seperate entries by spaces
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# passports can have a missing cid and still be valid, but must have all other field
# one list item must contain all passport elements, right now they are split by line



passPort = open('day4.input')
passPort2 = " ".join(line.strip() for line in passPort) 
passPort3 = passPort2.replace("  ", '\n')


l = passPort3.splitlines()

count = 0

for i in l:
    if 'byr' in i and 'iyr' in i and 'eyr' in i and 'hgt' in i and 'hcl' in i and 'ecl' in i and 'pid' in i:
        count += 1
    
print(count)



# if 'byr' and 'iyr' in i[x] and 'eyr' in i[x] and 'hgt' in i[x] and 'hcl' in i[x] and 'ecl' in i[x] and 'pid' in i[x]:
        # count += 1