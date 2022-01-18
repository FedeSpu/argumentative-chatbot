from ReadDataSet import ReadDataSet
import numpy as np

rdsEv = ReadDataSet()
dsEv = rdsEv.matrix
# Get all the evidence column
ev = dsEv['CDE']
# Remove duplicates
ev = list(dict.fromkeys(ev))
# Transform into array
evArr = np.array(ev)

file_name = "vocabularyRenforcement.npy"

load_file = np.load(file_name, allow_pickle=True)
vocabulary = load_file[2]
print("loaded")

for key in vocabulary.keys():
    print(key + "Has:")
    indices = np.where(vocabulary[key] == 1)
    for index in indices[0]:
        print("Line, index " + str(index) + " :" + str(evArr[index]))
    print("\n\n")


