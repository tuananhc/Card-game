from valid_table import comp10001huxxy_valid_table as vt

valdict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
           '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}
rdict = {value: key for key, value in valdict.items()}

def add_to_table(table, hand, active_player):
    joker = True
    play_list = []
    start, end = True, True 
    if not table: 
        return 
    for i in range(len(table)):
        if len(table[i]) < 3: 
            continue
        test = table[i].copy()
        if 'XX' in test:
            joker = True
            test.remove('XX')
        test = [(valdict[card[0]], card[1]) for card in test]
        test.sort()
        if test[0][0] == test[1][0]: 
            val = []
            for card in hand: 
                if card == 'XX': 
                    continue
                if card == test[0][0]: 
                    val.append(card)
            test = [rdict[card[0]]+ card[1] for card in test]
            if val:
                for card in val:  
                    test.append(card)
                    if vt(test):
                        if card in hand: 
                            play_list.append((active_player, 1, (card, i)))
                            break
                        else:
                            test.remove(card)
            if not joker:
                if 'XX' in hand:
                    if 'XX' not in test and len(test) < 8:
                        play_list.append((active_player, 1, ('XX', i)))
        else: 
            if not joker:
                if 'XX' in hand:
                    if len(test) < 13:
                        play_list.append((active_player, 1, ('XX', i)))
            if test[0][0] == 1:
                start = False
            if test[-1][0] == 13:
                end = False
            if test[0][1] in 'SC':
                if start: 
                    val = [rdict[test[0][0] - 1] + 'H', 
                           rdict[test[0][0] - 1] + 'D']
                    for card in val:    
                        if card in hand: 
                            play_list.append((active_player, 1, (card, i)))
                            break
            else:
                if start: 
                    val = [rdict[test[0][0] - 1] + 'S', 
                           rdict[test[0][0] - 1] + 'C']
                    for card in val:    
                        if card in hand: 
                            play_list.append((active_player, 1, (card, i)))
                            break
            if test[-1][1] in 'SC':
                if end: 
                    val = [rdict[test[-1][0] + 1] + 'H', 
                           rdict[test[-1][0] + 1] + 'D']
                    for card in val:    
                        if card in hand: 
                            play_list.append((active_player, 1, (card, i)))
                            break
            else:
                if end: 
                    val = [rdict[test[-1][0] + 1] + 'S', 
                           rdict[test[-1][0] + 1] + 'C']                     
                    for card in val:
                        if card in hand:
                            play_list.append((active_player, 1, (card, i))) 
                            break
    return play_list
