from sklearn.feature_extraction.text import *
from sklearn.metrics.pairwise import cosine_similarity


# Take an array of string (arr_voc) and the user input
def uniform_input(arr_voc, user_input):
    cv = CountVectorizer()
    matrix = cv.fit_transform(arr_voc)
    user_input_cv = cv.transform([user_input]).toarray()[0]
    res = []
    for i in range(len(matrix.toarray())):
        row = matrix.toarray()[i]
        rowSh = row.reshape(1, len(row))
        userSh = user_input_cv.reshape(1, len(user_input_cv))
        res.append((cosine_similarity(rowSh, userSh)[0][0], i))

    res.sort(reverse=True)
    print(res)
    if res[0][0] > 0.4:
        return list(arr_voc)[res[0][1]]
    else:
        return user_input
