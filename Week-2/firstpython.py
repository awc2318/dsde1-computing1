#Python
message = 'Person 1: Whats the password?'
password = "Person 2: He's not dead he's pining for the fjords"
print(message)
print(password)

import math
x = 3
y = 2 + math.sin(x)
print(y)

x = 5
z = math.log(x-3) + 2*(x+4)
print(z)

print('So what you doing here?')
Talk = input(' ')
print(Talk + ' really? You Sure?')

print('Say a number between 1 - 10')
guess = input('')
guess = int(guess)
import random
secret_num = random.randint(1,10)
for wd in range(1, 7):
    if guess == secret_num:
        print('World domination complete')
    else: 
        print('Nope')
        break