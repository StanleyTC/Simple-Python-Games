from time import sleep
import random

print('Welcome to Hangman Game!')
sleep(0.5)

# Here we will import a text file with the word we choosed to the game, 
#the name of the file is words.txt
words = []

arquivo = open('words.txt', 'r') #opening the file in read mode
for line in arquivo:
    line = line.strip()
    words.append(line) #add line to words during the for cycle
arquivo.close #now we have our secret words from the file at our program, but we will need to chose one with random function


number = random.randrange(0, len(words))
word = words[number].upper()  #now we have our random word

llist = []
for t in word:
    llist.append('-')
sleep(0.5)

enforcou = False
acertou = False
mistakes = 0

while(not enforcou and not acertou):
    position = 0
    guess = input('Type something: ').upper()

    if guess in word:
        for i in word:
            position += 1
            if guess.upper() == i.upper():
                print(f'I found the word {i.upper()} in position {position}')
                llist[position-1] = i.upper()
                print(llist)
    else:
        mistakes += 1
        if(mistakes == 1):
            print (" |      (_)   ")
            print (" |            ")
            print (" |            ")
            print (" |            ")

        if(mistakes == 2):
            print (" |      (_)   ")
            print (" |      \     ")
            print (" |            ")
            print (" |            ")

        if(mistakes == 3):
            print (" |      (_)   ")
            print (" |      \|    ")
            print (" |            ")
            print (" |            ")

        if(mistakes == 4):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |            ")
            print (" |            ")

        if(mistakes == 5):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |       |    ")
            print (" |            ")

        if(mistakes == 6):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |       |    ")
            print (" |      /     ")

        if (mistakes == 7):
            print (" |      (_)   ")
            print (" |      \|/   ")
            print (" |       |    ")
            print (" |      / \   ")


    
    #conditions for game over by loosing:
    if mistakes == 7:
        enforcou = True
    #conditions for game over by winning:
    if '-' not in llist:
        acertou = True

if enforcou == True:
    print('Game over, you lost the game...')
    print("    _______________         ")
    sleep(0.25)
    print("   /               \       ")
    sleep(0.25)
    print("  /                 \      ")
    sleep(0.25)
    print("//                   \/\  ")
    sleep(0.25)
    print("\|   XXXX     XXXX   | /   ")
    sleep(0.25)
    print(" |   XXXX     XXXX   |/     ")
    sleep(0.25)
    print(" |   XXX       XXX   |      ")
    sleep(0.25)
    print(" |                   |      ")
    sleep(0.25)
    print(" \__      XXX      __/     ")
    sleep(0.25)
    print("   |\     XXX     /|       ")
    sleep(0.25)
    print("   | |           | |        ")
    sleep(0.25)
    print("   | I I I I I I I |        ")
    sleep(0.25)
    print("   |  I I I I I I  |        ")
    sleep(0.25)
    print("   \_             _/       ")
    sleep(0.25)
    print("     \_         _/         ")
    sleep(0.25)
    print("       \_______/           ")
    sleep(0.25)
if acertou == True:
    print('Congratulations! you won the game!')
    sleep(0.5)
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
