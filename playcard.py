from score import comp10001huxxy_score as score
from add_to_table import add_to_table
from sort_hand import recur_next_card
from collections import defaultdict as dd

best_moves = []

def comp10001huxxy_bonus_play(play_history, active_player, hand, table):
    '''The function determines the best play, based on the player's hand, play
    history, and the current table state'''
    
    global best_moves
    play0 = []
    play1 = []
    valid = []
    valdict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
               '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}
    rdict = {value: key for key, value in valdict.items()}
    
    if 'XX' in hand: 
        hand.remove('XX')
        hand = [(valdict[x[0]], x[1]) for x in hand]
        hand.sort()  
        hand = [rdict[x[0]] + x[1] for x in hand]
        hand.append('XX')
    else:
        hand = [(valdict[x[0]], x[1]) for x in hand]
        hand.sort()  
        hand = [rdict[x[0]] + x[1] for x in hand]
    
    count = 0
    for play in play_history[::-1]:
        if play[0] != active_player:
            break
        count += 1
    
    play1 = add_to_table(table, hand, active_player)
    if play1:
        if len(play1) >= 6:
            play1 = play1[:7]   
    
    if count == 0:
        if not best_moves:
            count_card = dd(int)
            for card in hand: 
                if card == 'XX':
                    continue
                count_card[card] += 1

            same_d = {}
            for card in hand:
                if card == 'XX':
                    continue
                group = list(filter(lambda x: x[0] == card[0], hand))
                if len(group) < 3:
                    same_d[card] = group
                else:
                    if len(group) == len(set(group)):
                        same_d[card] = group
                    else: 
                        if len(set(group)) == 3:
                            same_d[card] = list(set(group))
                        if len(set(group)) == 4: 
                            if len(group) >= 6:
                                same_d[card] = group[:7]
                            else:
                                same_d[card] = group
            run_valid = []
            checked = ['XX']
            for card in hand:
                if card in checked: 
                    continue
                combinations = (recur_next_card(hand, card))
                if len(combinations) < 3:
                    continue
                for item in combinations: 
                    checked.append(item)
                    if item[1] in 'SC':
                        for item in list(filter(lambda x: x == item[0] + 'S' or 
                                                x == item[0] + 'C', hand)):
                            if item not in checked: 
                                checked.append(item)
                    else:
                        for item in list(filter(lambda x: x == item[0] + 'H' or 
                                                x == item[0] + 'D', hand)):
                            if item not in checked: 
                                checked.append(item)
                if len(combinations) >= 6:
                    run_valid.append(combinations[(len(combinations) - 6):])
                else:
                    run_valid.append(combinations)
            run_d = {}
            test = hand
            for group in run_valid:
                for card in group:
                    run_d[card] = group
                    test.remove(card)
            for card in test: 
                run_d[card] = [card]
            compare = {}
            for card in same_d:
                compare[card] = {'same': len(same_d[card]),
                                 'run': len(run_d[card])}
            checked = []
            for item in compare.items(): 
                if item[1]['same'] < 3 and item[1]['run'] <3:
                    continue
                if item[1]['same'] >= 3 and item[1]['run'] >= 3:
                    if (item[1]['run'] >= 4 and 
                        item[0] == run_d[item[0]][-1] or 
                        item[0] == run_d[item[0]][0]):
                            run_d[item[0]].remove(item[0])
                            if same_d[item[0]] not in valid:
                                valid.append(same_d[item[0]])
                            if run_d[item[0]] not in valid:
                                valid.append(run_d[item[0]])
                    else:
                        if score(same_d[item[0]]) > score(run_d[item[0]]):
                            if count_card[item[0]] == 1: 
                                checked.append(run_d[item[0]])
                            if same_d[item[0]] not in valid:
                                valid.append(same_d[item[0]])
                        else:
                            if count_card[item[0]] == 1: 
                                checked.append(same_d[item[0]])
                            if run_d[item[0]] not in valid:
                                valid.append(run_d[item[0]])
                else:
                    if item[1]['same'] >= 3 and item[1]['run'] < 3:
                        if same_d[item[0]] not in valid:
                            valid.append(same_d[item[0]])
                    if item[1]['run'] >= 3 and item[1]['same'] < 3:
                        if run_d[item[0]] not in valid:
                            valid.append(run_d[item[0]])
            if checked:
                for item in checked:
                    if item in valid:
                        valid.remove(item)
            if valid:
                for item in valid: 
                    if item not in play0:
                        play0.append(item)  
            play0.sort(reverse=True, key=lambda x: score(x))       

            if (active_player, 3, None) not in play_history:
                if play0:
                    if score(play0[0]) >= 24:
                        for i in range(len(play0[0])):
                            best_moves.append((active_player, 1, 
                                                   (play0[0][i], len(table))))
            else:
                for i in range(len(play0[0])):
                    best_moves.append((active_player, 1, 
                                           (play0[0][i], len(table))))
        if best_moves:
            return best_moves.pop(0)
        else:
            if play1 and (active_player, 3, None) in play_history:
                return play1.pop(0)
            else:
                return (active_player, 0, None)
            
    elif 0 < count < 6:
        if best_moves:
            return best_moves.pop(0)
        else:
            if play1:
                return play1.pop(0)
            else:
                return (active_player, 3, None)
    elif count == 6:
        return (active_player, 3, None)
