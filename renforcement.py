import random
import numpy as np
import os.path
import uniform_sim as unif

global eps
global i
global vocabulary

vocabulary = {}
file_name = "vocabularyRenforcement.npy"
i = 0
eps = 1

if os.path.exists(file_name):
    load_file = np.load(file_name, allow_pickle=True)
    vocabulary = load_file[2]
    eps = load_file[1]
    i = load_file[0]

rangeNum = 100


# n is the number of results wanted, indexDS is an array of index of DataSet already filtered by similarity
def getN(n, indexDS, lenDS, user_input):
    global i, eps, vocabulary
    res = []
    old_index = -1
    r = random.random()
    randIndex = random.sample(range(len(indexDS)), n)
    # This line check if the input is like one of the key of the vocabulary; if it's not, return the input
    if os.path.exists(file_name):
        user_input = unif.uniform_input(vocabulary.keys(), user_input)
    if user_input not in vocabulary:
        vocabulary[user_input] = np.zeros(lenDS, dtype=int)
    for j in range(n):
        # At 50% eps decrease until it reaches 0.2 at the end
        if i > rangeNum / 3:
            eps -= 1/(rangeNum/2)

        if r < eps:
            # Random choice on input array of index
            index = randIndex[j]  # random.randrange(len(indexDS))
            res_tmp = indexDS[index]
        else:
            # Choice by old knowledge
            # Get lower index in old knowledge while index is in the filtered array
            list_copy = vocabulary[user_input].copy()
            while True:
                index = np.argmax(list_copy)
                if index == 0 and index not in res:
                    res_tmp = indexDS[randIndex[j]]
                    break
                elif index in res:
                    list_copy[np.argmax(list_copy)] = 0
                else:
                    res_tmp = index
                    break
                """
                # If the choice of user is not in filtered 
                if index == 0:
                    index = randIndex[j]
                    break
                if index in indexDS:
                    break
                else:
                    list_copy[np.argmax(list_copy)] = 0"""
        i += 1
        res.append(res_tmp)
    return res


def increase(user_input, index):
    user_input = unif.uniform_input(vocabulary.keys(), user_input)
    vocabulary[user_input][index] += 1
    save_vocabulary()


def save_vocabulary():
    np.save(file_name, [i, eps, vocabulary])
