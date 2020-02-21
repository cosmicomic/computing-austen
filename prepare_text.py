import re
import string
from scipy import sparse
from sklearn.cluster import KMeans

with open("Corpus/Northanger excerpt.txt", encoding="utf8") as f:
    northanger_text = f.read()

# remove chapter headings
new_text = northanger_text
matches = re.findall("CHAPTER \d+|Chapter \d+", northanger_text)
for match in matches:
    new_text = re.sub(match, '', new_text)

# compile set of bigrams
words = re.split(r'\W+', new_text)
words = [word.lower() for word in words if word != ""]

bigrams = []

for i in range(len(words) - 1):
    bigrams.append((words[i], words[i + 1]))

bigrams = list(set(bigrams))

# prepare sentences
sentences = re.split(r'[?.!]', new_text)

# remove punctuation
remove_punct = []

for sentence in sentences:
    new_sentence_chars = []
    for c in sentence:
        if c == "\n" or c == "-" or c == '\ufeff':
            new_sentence_chars.append(" ")
        elif c in string.punctuation:
            continue
        else:
            new_sentence_chars.append(c.lower())
    new_sentence = "".join(new_sentence_chars)
    remove_punct.append(new_sentence.strip())

samples = []

# convert sentences into sets of bigrams
for sentence in remove_punct:
    tokenized_sentence = re.split(r'\W+', sentence)
    bigram_set = []

    for i in range(len(tokenized_sentence) - 1):
        bigram_set.append((tokenized_sentence[i], tokenized_sentence[i + 1]))

    samples.append(bigram_set)

# create a feature (bigram) vector for each sentence

# represent as sparse vectors
n_features = len(bigrams)
n_samples = len(samples)

# construct sparse matrix
X = sparse.lil_matrix((n_samples, n_features))
positives = 0

for i in range(n_samples):
    for j in range(n_features):
        if bigrams[j] in samples[i]:
            positives += 1
            print(i, j, bigrams[j])
            X[i, j] = 1

# cluster
kmeans = KMeans(n_clusters=4).fit(X)
print(kmeans.labels_)