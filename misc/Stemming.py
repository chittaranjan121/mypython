import nltk
from nltk.stem import PorterStemmer

stemmer=PorterStemmer()
words=["Running","runner","ran","easily","fairly"]
s=[stemmer.stem(i) for i in words]
print(s)
