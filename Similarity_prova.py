from sklearn.feature_extraction.text import *
from sklearn.metrics.pairwise import cosine_similarity

# vectorization
docs = []
f = open("prova1", "r")
line = f.read()
docs.append(line)
f.close()
f = open("prova2", "r")
line = f.read()
docs.append(line)
f.close()

cv = CountVectorizer()
x = cv.fit_transform(docs)
print(cv.get_feature_names())
print(x.toarray())
testo = ['videogames are fine']
testoX = cv.transform(testo)
print(testoX.toarray())
res = []
for i in range(0, len(x.toarray())):
    row = x.toarray()[i]
    index = i
    rowSh = row.reshape(1, len(row))
    testoSh = (testoX.toarray()[0]).reshape(1, 7)
    res.append((cosine_similarity(rowSh, testoSh)[0][0], i))

res.sort(reverse=True)
print(res)
best = docs[res[0][1]]
print(best)

print(cv.vocabulary_)
# saved file in npy -> only load
# np.load(nome.npy, allow_pickle=True).item()
