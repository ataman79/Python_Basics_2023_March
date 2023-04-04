from string import ascii_letters, digits, punctuation

import random

password_signs = ascii_letters + digits + punctuation

password_lenght = 10

password = ''.join(random.sample(password_signs, password_lenght))

print("Your new generated password is: ", password )