def valid_table(groups):
    if len(groups) == 0:
        return True
    for group in groups:
        if len(group) < 3: 
            return False
        valdict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
                   '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}
        cards = [(valdict[x[0]], x[1]) for x in group]
        cards.sort()
        val = [x[0] for x in cards]
        suit = [x[1] for x in cards]
        if len(group) <= 4:
            if len(suit) != len(set(suit)):
                return False
        for i in range(len(val) - 1):
            if val[i] != val[i + 1]:
                if int(val[i]) + 1 != int(val[i + 1]):
                    return False
                if suit[i] in 'SC' and suit[i + 1] in 'HD':
                    continue
                elif suit[i] in 'HD' and suit[i + 1] in 'SC':
                    continue
                else:
                    return False
            if len(group) >= 4:
                if len(set(suit)) < 4:
                    return False
    return True
