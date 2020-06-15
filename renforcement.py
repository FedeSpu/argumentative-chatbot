import random
import numpy as np

global eps
# TODO: save i var
global i

vocabulary = {}
eps = 1
i = 0
rangeNum = 100


# n is the number of results wanted, indexDS is an array of index of DataSet already filtered by similarity
def getN(n, indexDS, lenDS, user_input):
    res = []
    for j in range(n):
        # At 50% eps decrease until it reaches 0.2 at the end
        if i > rangeNum / 3:
            eps -= 1/(rangeNum/2)
        r = random.random()

        # TODO: uniform user_input by similarity
        if user_input not in vocabulary:
            vocabulary[user_input] = np.zeros(lenDS, dtype=int)
        if r < eps:
            # Random choice on input array of index
            index = random.randrange(len(indexDS))
        else:
            # Choice by old knowledge
            # Get lower index in old knowledge while index is in the filtered array
            while True:
                index = np.argmax(vocabulary[user_input])
                if index in indexDS:
                    break
        res_tmp = indexDS[index]
        i += 1
        res[j] = res_tmp
    return res
