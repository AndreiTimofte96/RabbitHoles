#!/usr/bin/python
import sys
import random

groundLength = int(sys.argv[1])

def printGround(rabbitPosition, userGuess):
    ground = ''
    for index in range(groundLength):
        if index == rabbitPosition:
            ground += 'x'
        elif index == userGuess:
            ground += 'o'
        else:
            ground += '_'
        ground += ' '

    print(ground)
    print(' '.join([str(index) for index in range(groundLength)]))
    print


def main():
    rabbitPosition = random.randint(0, groundLength - 1)
    initialRabbitPosition = rabbitPosition
    allRabbitPosition = []
    allGuessesPosition = []
    AIGuesses = solver()
    AIGuessIndex = 0

    while True:
        # printGround(rabbitPosition, -1)
        allRabbitPosition.append(rabbitPosition)

        # guess = input("Ghiceste pozitia: ")

        guess = AIGuesses[AIGuessIndex]
        AIGuessIndex += 1
        allGuessesPosition.append(guess)

        if guess == rabbitPosition:
            break

        randomPosition = random.choice([-1, 1])

        if randomPosition == 1:
            if rabbitPosition + 1 < groundLength:
                rabbitPosition += 1
            else:
                rabbitPosition -= 1

        if randomPosition == -1:
            if rabbitPosition - 1 >= 0:
                rabbitPosition -= 1
            else:
                rabbitPosition += 1

    # for index in range(len(allRabbitPosition)):
    #     printGround(allRabbitPosition[index], allGuessesPosition[index])

    print('\nAi ghicit pozitia din ' + str(len(allGuessesPosition)) +
          ' incercari!')
    print('Pozitia initiala a fost ' + str(initialRabbitPosition) + '.')
    print('Numar total de incercari: ' +  str(len(AIGuesses)) + '.')


def solver():
    guesses = []
    step = 'double'
    for index in range(groundLength - 1, 0, -2):
        if step == 'double':
            guesses.extend([index, index - 1, index, index - 1])
            step = 'single'
        else:
            guesses.extend([index, index - 1])
            step = 'double'

    for index in range(groundLength - 2, 0, -2):
        guesses.extend([index, index - 1, index, index - 1])
    # print(guesses)
    return guesses


main()