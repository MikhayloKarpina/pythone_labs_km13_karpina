suit = ("diamonds", "club", "hart", "spades")

value0 = tuple("A")
value1 = tuple(range(2, 11))
value2 = ("J", "Q", "K")
value = value0 + value1 + value2

card = []
for i in suit:
    for j in value:
        card.append((j, i))

for i in card:
    print(i)