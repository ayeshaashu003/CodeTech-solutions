import random
import array
import time
Max_Len=10
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
Lowercase_Char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
Upcase_Char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
Symbols= ['@', '#', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '<']

COMBINED_LIST = Numbers + Upcase_Char + Lowercase_Char + Symbols
rand_digit = random.choice(Numbers)
rand_upper = random.choice(Upcase_Char)
rand_lower = random.choice(Lowercase_Char)
rand_symbol = random.choice(Symbols)

# at this stage, the password contains only 4 characters but  we want a 10-character password
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(Max_Len- 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
# traverse the temporary password array and append the chars to form the password
password = ""
for x in temp_pass_list:
        password = password + x

time.sleep(0.2)
print('your password is:',password)
