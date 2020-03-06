import re
import random
import string
import numpy as np

from collections import Counter

from scipy import sparse
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from joblib import dump, load
import markovify

def draw_from_cluster(n, cluster, samples, sentences=False):
    for _ in range(n):
        cluster_index = random.randrange(0, len(cluster))
        sentence_index = cluster[cluster_index]
        if not sentences:
            print(' '.join(samples[sentence_index]) + '.')
        else:
            printed_sentence = samples[sentence_index].replace("\n", " ")
            print(printed_sentence)

def prepare_text(title_string):
    with open("Corpus/" + title_string + ".txt", encoding="utf8") as f:
        text = f.read()

    # remove chapter headings
    new_text = text
    matches = re.findall("CHAPTER \w+|Chapter \w+", text)
    for match in matches:
        new_text = re.sub(match, '', new_text)

    # remove periods from end of titles
    new_text = new_text.replace("Mrs.", "Mrs")
    new_text = new_text.replace("Mr.", "Mr")
    new_text = new_text.replace("Dr.", "Dr")

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

    return sentences, samples

def cluster(k, ngrams, samples, title_string):
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
    kmeans = KMeans(n_clusters=k).fit(X)
    dump(kmeans, 'kmeans_' + title_string + '.joblib') 
    print(kmeans.labels_)

    labels = kmeans.labels_
    unique, counts = np.unique(labels, return_counts=True)
    print(dict(zip(unique, counts)))

    return kmeans

def show_cluster_sentences(n, sentences, labels):
    cluster_dict = {}
    for i in range(len(sentences)):
        if labels[i] not in cluster_dict:
            cluster_dict[labels[i]] = [i]
        else:
            cluster_dict[labels[i]].append(i)

    for key in cluster_dict.keys():
        print("Cluster", key)
        draw_from_cluster(5, cluster_dict[key], sentences, True)
        print("\n")

def sort_samples_by_cluster(labels, samples):
    cluster_dict = {}
    for i in range(len(samples)):
        if labels[i] not in cluster_dict:
            cluster_dict[labels[i]] = [samples[i]]
        else:
            cluster_dict[labels[i]].append(samples[i])

    return cluster_dict

def get_bags_of_words(cluster_dict):
    bag_dict = {}
    for cluster_index in cluster_dict.keys():
        bag_of_words = []
        sentences = cluster_dict[cluster_index]
        for sentence in sentences:
            bag_of_words += re.split(r'\W+', sentence)
        bag_dict[cluster_index] = bag_of_words
    return bag_dict


k = 5
title_string = "Persuasion"
new_text = prepare_text(title_string)
sentences, samples = prepare_samples(new_text)
unigrams = get_unigrams(new_text)
# kmeans = cluster(5, unigrams, samples, title_string)
kmeans = load('kmeans_persuasion.joblib')
labels = kmeans.labels_
unique, counts = np.unique(labels, return_counts=True)
cluster_sizes = dict(zip(unique, counts))

transitions = np.zeros((k, k))
for i in range(1, len(samples)):
    curr = labels[i]
    prev = labels[i - 1]
    transitions[prev][curr] += 1

transitions_normalized = np.array([transitions[0] / cluster_sizes[0]])
for i in range(1, k):
    add_row = np.array([transitions[i] / cluster_sizes[i]])
    transitions_normalized = np.concatenate((transitions_normalized, add_row))

transitions_list = transitions_normalized.tolist()
print(transitions_list)

gen_sequence = [4]
prev = gen_sequence[0]
for i in range(1, 8):
    print("prev", prev)
    next = random.choices(list(range(k)), weights=transitions_list[prev])[0]
    gen_sequence.append(next)
    prev = next

print(gen_sequence)

cluster_dict = sort_samples_by_cluster(labels, sentences)
markov_chains = []

for key in cluster_dict.keys():
    cluster_continuous = '. '.join(cluster_dict[key])
    text_model = markovify.Text(cluster_continuous, state_size=2)
    markov_chains.append(text_model)

sentence_sequence = []

for state in gen_sequence:
    state_model = markov_chains[state]
    sentence_sequence.append(text_model.make_sentence())

print(" ".join(sentence_sequence))



# show_cluster_sentences(10, sentences, labels)

# cluster_dict = sort_samples_by_cluster(labels, sentences)

# for key in cluster_dict.keys():
#     cluster_continuous = '. '.join(cluster_dict[key])
#     text_model = markovify.Text(cluster_continuous, state_size=2)

#     print("CLUSTER", key)
#     for i in range(5):
#         print(text_model.make_sentence())
# bag_dict = get_bags_of_words(cluster_dict)

# c = Counter(bag_dict[0])
# frequent1 = [word for (word, _) in c.most_common(50)]
# print(frequent1)

# c = Counter(bag_dict[1])
# frequent2 = [word for (word, _) in c.most_common(50)]
# print(frequent2)

# print(set(frequent1).intersection(set(frequent2)))
