import itertools as it

def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for x in range(6):
        for y in range(6):
            if dice1[x]>dice2[y]:
                dice1_wins+=1
            elif dice2[y]>dice1[x]:
                dice2_wins+=1
    return (dice1_wins, dice2_wins)

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    not_bestdices=[]
    for comb in it.combinations(range(len(dices)),2):
        (dices1_wins,dices2_wins)=count_wins(dices[comb[0]],dices[comb[1]])
        if dices1_wins>dices2_wins:
            if not comb[1] in not_bestdices:
                not_bestdices.append(comb[1])
        elif dices1_wins<dices2_wins:
            if not comb[0] in not_bestdices:
                not_bestdices.append(comb[0])
    if len(not_bestdices)==len(dices):
        return -1
    else:
        for x in range(len(dices)):
            if not x in not_bestdices:
                return x


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    best_dice=find_the_best_dice(dices)
    if best_dice!=-1:
        strategy["first_dice"] = best_dice
    else:
        strategy["choose_first"] = False
        for i in range(len(dices)):
            for x in range(len(dices)):
                if x == i:
                    continue
                (first,second)=count_wins(dices[i],dices[x])
                if second>first:
                    strategy[i]=x
    return strategy

dices= [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
print(find_the_best_dice(dices))