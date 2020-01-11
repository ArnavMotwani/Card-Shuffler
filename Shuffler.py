import random
Cards = [""]*52
number = 1
count = 0
cnt = 1

#Initializing the array with only the card number
for i in range(52):
    if count == 4:
        number = number + 1
        count = 0
    if number <= 9:
        Cards[i] = "0" + str(number)
    else:
        Cards[i] = str(number)
    count = count + 1

#Adding the suite of the card to the array
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

#Shuffling and the printing the deck (remove the lines 33 and 34 if you dont want the deck to print)
random.shuffle(Cards)
for v in range(52):
    print(Cards[v])