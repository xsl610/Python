from random import *
temp_list = []
card = []
for i in range(2, 11):
    temp_list.append(i)
temp_list.extend(["J", "Q", "k", "A"])
for i in temp_list:
    for card_type in ["黑桃", "红桃", "方块", "草花"]:
        a = (card_type, i)
        card.append(a)
shuffle(card)
print(card)
