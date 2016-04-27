import random
darts = [i for i in range(1000,10000)]

random.shuffle(darts)

print(darts[:5])

dartsAftShuffle = []

while len(dartsAftShuffle) <5:
    dartsAftShuffle.append(darts[0])
    del darts[0]

print (dartsAftShuffle)
