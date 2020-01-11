import random
Cards = [""]*52
number = 1
count = 0
cnt = 1
for i in range(52):
    if count == 4:
        number = number + 1
        count = 0
    if number <= 9:
        Cards[i] = "0" + str(number)
    else:
        Cards[i] = str(number)
    count = count + 1

for s in range(52):
    if cnt == 1:
        Cards[s] = Cards[s] + " - S"
    if cnt == 2:
        Cards[s] = Cards[s] + " - H"
    if cnt == 3:
        Cards[s] = Cards[s] + " - C"
    if cnt == 4:
        Cards[s] = Cards[s] + " - D"
        cnt = 1
    cnt = cnt + 1

random.shuffle(Cards)
for v in range(52):
    print(Cards[v])