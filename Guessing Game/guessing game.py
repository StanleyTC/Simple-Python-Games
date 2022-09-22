from time import sleep 
from random import randint
print('Welcome to guessing game! you should try to guess what number I am thinking ')
sleep(0.5)

secret_word = randint(0, 10)
count = 1
guessing = int(input('Please, type a number from 0 to 10: '))
sleep(0.5)
print('Processing...')
sleep(1)

while secret_word != guessing:    
    guessing = int(input('you missed! that is not the number I thought, try again: '))
    sleep(0.5)
    print('Processing...')
    count += 1

print(f'You are right! I really thought about the number {secret_word}, you needed {count} attempts')
