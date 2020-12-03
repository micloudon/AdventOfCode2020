import re

# Divide line into 3 parts
# ex. 2-5 j: bjjjj
# must contain between 2-5 'j' to be valid, this example is valid
# ex. 2-3 a: abcde, must contain between 2-3 'a' to valid, this example is invalid

x = 0

passWords = open('day2.input')
for line in passWords:    
    policy = re.findall(r'\d+', line)
    policy = [int(i) for i in policy] 
    letter = re.findall(r'(?i)\b[a-z]\b', line)
    word = re.findall(r'\b[a-z]*$\b', line)
    # print(policy, letter, word)

    counter = word[0].count(letter[0])
    if counter in range(policy[0], policy[1]+1):
        x += 1
        print(word, x)

    



    
    


