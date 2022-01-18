import uniform_sim as sim
import os.path
import numpy as np

file_name = "vocabularyRenforcement.npy"
file_name2 = "vocabularyRenforcement3.npy"
vocabulary = {}
vocabulary2 = {}
esp = 0
i = 0

if os.path.exists(file_name) and os.path.exists(file_name2):
    load_file = np.load(file_name, allow_pickle=True)
    load_file2 = np.load(file_name2, allow_pickle=True)
    vocabulary = load_file[2]
    vocabulary2 = load_file2[2]
    print("loaded")

for key in vocabulary2.keys():
    lenDS = len(vocabulary2[key])
    key_unif = sim.uniform_input(vocabulary.keys(), key)
    if key_unif not in vocabulary:
        vocabulary[key_unif] = vocabulary2[key]
    else:
        vocabulary[key_unif] = np.sum([vocabulary[key_unif], vocabulary2[key]], axis=0)

print("Finish")
