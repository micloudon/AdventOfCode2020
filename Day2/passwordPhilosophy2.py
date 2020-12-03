import re

# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

x = 0
y = 0
passWords = open('day2.input')
for line in passWords:    
    policy = re.findall(r'\d+', line)
    policy = [int(i) for i in policy] 
    letter = re.findall(r'(?i)\b[a-z]\b', line)
    word = re.findall(r'\b[a-z]*$\b', line)

    letter = letter[0]
    word = word[0]

    policy1 = policy[0]
    policy2 = policy[1]
    y += 1

    if letter in word[policy1-1] and letter not in word[policy2-1] or letter in word[policy2-1] and letter not in word[policy1-1]: 
            x +=1
            print(y, word, x)
        