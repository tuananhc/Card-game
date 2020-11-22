def huxxy_score(cards):
    '''The function takes a list of cards and calculates their sum'''
    valdict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
               '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}
    return sum([valdict[card[0]] for card in cards])   
