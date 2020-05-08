from sklearn.feature_extraction.text import *
from sklearn.metrics.pairwise import cosine_similarity
from ReadDataSet import ReadDataSet
import numpy as np
import os.path


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
    best = res[:n]
    # Old method: best_res = map(lambda el: (evArr[el[1]], el[0]), best) and after list(best_res)
    # print(list(best_res))
    best_res = [(evArr[item[1]], item[0]) for item in best]
    # Best one (string, confidence)
    return best_res

