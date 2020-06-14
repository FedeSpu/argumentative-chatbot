import random
import numpy as np

global eps

vocabulary = {}
eps = 1
rangeNum = 100
right = 0


def getN(n, dataset, inputU):
    for i in range(rangeNum):
        # At 50% eps decrease until it reaches 0.2 at the end
        if i > rangeNum / 3:
            eps -= 1/(rangeNum/2)
        r = random.random()

        if inputU not in vocabulary:
            vocabulary[inputU] = np.zeros(len(dataset), dtype=int)
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