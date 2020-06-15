from sklearn.feature_extraction.text import *
from sklearn.metrics.pairwise import cosine_similarity
from ReadDataSet import ReadDataSet
import numpy as np
import os.path
import renforcement as renf


def __get_cv(file_name, arr):
    cv = CountVectorizer()
    if os.path.exists(file_name):
        vocabulary = np.load(file_name, allow_pickle=True).item()
        cv.vocabulary_ = vocabulary
        matrix = cv.transform(arr)
        return cv, matrix
    else:
        matrix = cv.fit_transform(arr)
        np.save(file_name, cv.vocabulary_)
        return cv, matrix


rdsEv = ReadDataSet()
dsEv = rdsEv.matrix
# Get all the evidence column
ev = dsEv['CDE']
# Remove duplicates
ev = list(dict.fromkeys(ev))
# Transform into array
evArr = np.array(ev)

# Save a vocabulary if the file doesn't exist
cvEv, matrix = __get_cv("modelEv.npy", evArr)


# Get very long time
def get_n_similarity_ev(user_input, n):
    user = cvEv.transform([user_input]).toarray()[0]
    res = []
    for i in range(0, len(matrix.toarray())):
        row = matrix.toarray()[i]
        index = i
        rowSh = row.reshape(1, len(row))
        userSh = user.reshape(1, len(user))
        res.append((cosine_similarity(rowSh, userSh)[0][0], i))
    res.sort(reverse=True)
    # Cosine similarity filter n*4 result, the n filter is renforcement
    best = res[:n*4]
    # After filtering with cosine similarity, call renforcement learning
    indices = renf.getN(n, [item[1] for item in best], len(matrix.toarray()), user_input)
    best = [item for item in best if item[1] in indices]
    best_res = [(evArr[item[1]], item[0], item[1]) for item in best]
    # Best one (string, confidence)
    return best_res

