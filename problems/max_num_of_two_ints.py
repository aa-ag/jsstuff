############------------ IMPORTS ------------############
from itertools import combinations


############------------ FUNCTIONS ------------############
def maximum_number_of_two_digit_integers():
    '''
     creates deck of 90 cards
     lists all possible pair-combinations such that 
     each pair sum 100; provides count of 
     all pais that don't
    '''
    pair = list()

    cards = range(10, 91, 1)

    for i in list(combinations(cards, 2)):
        if i[0] + i[1] == 100:
            pair.append(i)

    return len(pair)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    print(maximum_number_of_two_digit_integers())