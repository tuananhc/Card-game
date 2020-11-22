valdict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
           '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}
rdict = {value: key for key, value in valdict.items()}

def next_card(hand, card):
    nextcard = []
    if card[1] in 'SC' and card[0] != 'K':
        nextcard.append(rdict[valdict[card[0]] + 1] + 'H')
        nextcard.append(rdict[valdict[card[0]] + 1] + 'D')
        for val in nextcard: 
            if val in hand: 
                return val
    elif card[1] in 'HD' and card[0] != 'K':
        nextcard.append(rdict[valdict[card[0]] + 1] + 'S')
        nextcard.append(rdict[valdict[card[0]] + 1] + 'C')
        for val in nextcard: 
            if val in hand: 
                return val
    return 

def prev_card(hand, card):
    prevcard = []
    if card[1] in 'SC' and card[0] != 'A':
        prevcard.append(rdict[valdict[card[0]] - 1] + 'H')
        prevcard.append(rdict[valdict[card[0]] - 1] + 'D')
        for val in prevcard: 
            if val in hand: 
                return val
    elif card[1] in 'HD' and card[0] != 'A':
        prevcard.append(rdict[valdict[card[0]] - 1] + 'S')
        prevcard.append(rdict[valdict[card[0]] - 1] + 'C')
        for val in prevcard: 
            if val in hand: 
                return val
    return 

def recur_next_card(hand, card): 
    val = next_card(hand, card)
    if not val:
        return [card]
    else: 
        return [card] + recur_next_card(hand[1:], val)

def recur_prev_card(hand, card): 
    val = prev_card(hand, card)
    if not val:
        return [card]
    else: 
        return [card] + recur_prev_card(hand[1:], val)