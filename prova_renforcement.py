# EPSILON GREEDY (TEST)
import random
import numpy as np
dataset = ["videogames", "politics", "economics", "arts", "news", "abortion", "university", "school", "games", "spread"]
inputUser = [("gamer", [0, 8]),
             ("salesman", [2, 9, 4]),
             ("student", [7, 6, 4])]

vocabulary = {}
eps = 1
rangeNum = 10000
right = 0
for i in range(rangeNum):
    # At 50% eps decrease until it reaches 0.2 at the end
    if i > rangeNum / 3:
        eps -= 1/(rangeNum/2)
    r = random.random()
    userRand = inputUser[random.randrange(3)]
    dataUser = userRand[1]

    if userRand[0] not in vocabulary:
        vocabulary[userRand[0]] = np.zeros(len(dataset), dtype=int)
    if r < eps:
        # Random choise on dataset
        index = random.randrange(10)
    else:
        # Choise by old knowledge
        index = np.argmax(vocabulary[userRand[0]])

    if index in dataUser:
        vocabulary[userRand[0]][index] += 1
        right += 1

print(vocabulary)
print("Percentage: " + str((right/rangeNum)*100) + "%")
