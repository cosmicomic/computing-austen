import re
import random
import string
import numpy as np

from scipy import sparse
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from joblib import dump, load

def draw_from_cluster(n, cluster, samples):
    for _ in range(n):
        cluster_index = random.randrange(0, len(cluster))
        sentence_index = cluster[cluster_index]
        print(' '.join(samples[sentence_index]) + '.')

def prepare_text():
    with open("Corpus/Northanger.txt", encoding="utf8") as f:
        northanger_text = f.read()

    # remove chapter headings
    new_text = northanger_text
    matches = re.findall("CHAPTER \d+|Chapter \d+", northanger_text)
    for match in matches:
        new_text = re.sub(match, '', new_text)

    return new_text

def get_unigrams(new_text):
    words = re.split(r'\W+', new_text)
    words = [word.lower() for word in words if word != ""]
    return list(set(words))

def prepare_samples(new_text):
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

    # convert sentences into sets of unigrams
    for sentence in remove_punct:
        tokenized_sentence = re.split(r'\W+', sentence)
        samples.append(tokenized_sentence)

    return samples

def cluster(k, ngrams, samples):
    # represent as sparse vectors
    n_features = len(ngrams)
    n_samples = len(samples)

    # construct sparse matrix
    X = sparse.lil_matrix((n_samples, n_features))

    # create a feature (unigram) vector for each sentence
    print("Filling out matrix")
    for i in range(n_samples):
        for j in range(n_features):
            if unigrams[j] in samples[i]:
                X[i, j] = 1

    print("Clustering")
    # cluster
    kmeans = KMeans(n_clusters=4).fit(X)
    dump(kmeans, 'kmeans.joblib') 
    print(kmeans.labels_)

    labels = kmeans.labels_
    unique, counts = np.unique(labels, return_counts=True)
    print(dict(zip(unique, counts)))

new_text = prepare_text()
samples = prepare_samples(new_text)

kmeans = load('kmeans.joblib')
labels = kmeans.labels_

cluster_dict = {}
for i in range(len(samples)):
    if labels[i] not in cluster_dict:
        cluster_dict[labels[i]] = [i]
    else:
        cluster_dict[labels[i]].append(i)

for key in cluster_dict.keys():
    print(key)
    draw_from_cluster(10, cluster_dict[key], samples)
    print("\n")