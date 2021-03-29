## 21 - Rock, Paper, Scissor Game

import random, sys

print("\n:: Rock + Paper + Scissors ::\n")

def gamePlay():
    # Initialize Win, Loss & Tie Variables.
    win = 0
    loss = 0
    tie = 0

    # Loop GamePlays.
    # while True:
    print(f'Win: {win} | Losses: {loss} | Ties: {tie}')
    print("""\nEnter Your Move:\n
        [1] - Rock 
        [2] - Paper 
        [3] - Scissors 
        [4] - Quit Game\n""")
    uSelection = int(input('\nType your Selection: '))

    userMove = userSelection(uSelection)
    cpuMove = randomCPU()
    tallyCount = checkWins(userMove, cpuMove)

    if tally == 1:
        tie += 1
    elif tally == 2:
        win += 1
    elif tally == 3:
        loss += 1
    
    
    # replay = input('\nPlay Again (y/n)?: ').lower
    # if replay == 'y':
    #     print('Replay!\n')
    #     gamePlay()
    # else:
    #     print('Thanks for playing!\n')

# User Selection method
def userSelection(uSelection):    
    if uSelection == 1:
        userMove = 'r'
        print("Your Selection:\tRock")
        return userMove
    elif uSelection == 2:
        userMove = 'p'
        print("Your Selection:\tPaper")
        return userMove
    elif uSelection == 3:
        userMove = 's'
        print("Your Selection:\tScissors")
        return userMove
    elif uSelection == 4:
        print('\nThanks for playing!!\n')
        # Quit the Game Loop - exit()
        sys.exit()
    else:
        print('\tInvalid Selection! CPU Wins\n')
        sys.exit()
    

# Random CPU Selection
def randomCPU():
    randomizeNum = random.randint(1, 3)

    # Display CPU Selection: 
    if randomizeNum == 1:
        cpuMove = 'r'
        print("CPU Selection:\tRock")
        return cpuMove
    elif randomizeNum == 2:
        cpuMove = 'p'
        print("CPU Selection:\tPaper")
        return cpuMove
    elif randomizeNum == 3:
        cpuMove = 's'
        print("CPU Selection:\tScissors")
        return cpuMove

# Check Win + Game Counters
def checkWins(userMove, cpuMove):
    if userMove == cpuMove:
        print("It is tie:!")
        tie = 1
        return tie
    elif userMove == 'r' and cpuMove == 's':
        print("You Win!")
        win = 2
        return win
    elif userMove == "p" and cpuMove == 'r':
        win = 2
        print("You Win!")
        return win
    elif userMove == "s" and cpuMove == 'p':
        win = 2
        print("You Win!")
        return win
    elif userMove == "r" and cpuMove == 'p':
        loss = 3
        print("You Lose!")
        return loss
    elif userMove == "p" and cpuMove == 's':
        loss = 3
        print("You Lose!")
        return loss
    elif userMove == "s" and cpuMove == 'r':
        loss = 3
        print("You Lose!")
        return loss

## Solution 21
gamePlay()