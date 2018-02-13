import random

def main():

    won = play()
    if won:
        print('You win!')
    else:
        print('You lose!')

def play():
    '''roll dice. only return as True is the random number rolled is greater than 4, else
    return false and user loses game.
    '''
    number_rolled = roll()
    print('You rolled a %d' % number_rolled)
    return number_rolled >= 4

def roll():
    return random.randint(1, 6)

if __name__ == '__main__':
    main()
