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
from hmmlearn import hmm

# Picks random sentences from a cluster and prints them to give an impression of
# what the cluster is about. Input can be in the format of a list of sentence strings,
# or a list of lists of words, which represent sentences.
def draw_from_cluster(n, cluster, samples, sentences=False):
    for _ in range(n):
        cluster_index = random.randrange(0, len(cluster))
        sentence_index = cluster[cluster_index]
        if not sentences:
            print(' '.join(samples[sentence_index]) + '.')
        else:
            printed_sentence = samples[sentence_index].replace("\n", " ")
            print(printed_sentence)

# Given the name of the book (which must be a file in the directory),
# performs pre-processing for clustering, which includes removing
# chapter headings, and removing periods from the ends of titles, such
# as Mrs. and Dr. This is because a later function breaks the text 
# into sentences using punctuation (., !, or ?), and keeping the
# periods at the ends of titles would mess this up.
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

# Given the full text of the novel as a single string, returns a list
# of the set of unique unigrams in the text.
def get_unigrams(new_text):
    words = re.split(r'\W+', new_text)
    words = [word.lower() for word in words if word != ""]
    return list(set(words))

# Given a list of sentence strings, returns a list of the same sentences
# but with some formatting (newlines, dashes, and \ufeff, whatever that is)
# removed.
def remove_punctuation(sentence_list):
    remove_punct = []

    for sentence in sentence_list:
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

    return remove_punct

# Converts a list of sentence strings to a list of lists of words,
# which are the same sentences.
def sentences_to_unigrams(sentences):
    samples = []
    for sentence in sentences:
        tokenized_sentence = re.split(r'\W+', sentence)
        samples.append(tokenized_sentence)

    return samples

# Given the text of the novel as a single string, returns it as a
# list of its sentences, and a list of lists of words, which are
# the same sentences.
def prepare_samples(new_text):
    # prepare sentences
    sentences = re.split(r'[?.!]', new_text)

    # remove punctuation
    remove_punct = remove_punctuation(sentences)

    # convert sentences into sets of unigrams
    samples = sentences_to_unigrams(remove_punct)

    return sentences, samples

# Input:
# - k (the number of clusters)
# - ngrams (the set of unique ngrams, which will be used as features in the vectors)
# - samples (a list of lists of words, which make up sentences)
# - title_string (the name the model will be saved under as a file)
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

# Given a list of sentences and the corresponding list of cluster labels,
# print 5 random sentences from each cluster to the terminal.
def show_cluster_sentences(sentences, labels):
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

# Given a list of samples and the corresponding list of labels,
# return a dictionary where the key is a cluster label, and the value
# is the set of all samples that belong to that cluster.
def sort_samples_by_cluster(labels, samples):
    cluster_dict = {}
    for i in range(len(samples)):
        if labels[i] not in cluster_dict:
            cluster_dict[labels[i]] = [samples[i]]
        else:
            cluster_dict[labels[i]].append(samples[i])

    return cluster_dict

# Given a dictionary mapping cluster labels to sets of samples
# that belong to the corresponding cluster, return a dictionary
# mapping cluster labels to sets of words in the corresponding cluster.
#
# This is useful for word cloud analysis.
def get_bags_of_words(cluster_dict):
    bag_dict = {}
    for cluster_index in cluster_dict.keys():
        bag_of_words = []
        sentences = cluster_dict[cluster_index]
        for sentence in sentences:
            bag_of_words += re.split(r'\W+', sentence)
        bag_dict[cluster_index] = bag_of_words
    return bag_dict


# Prepare the text and run k-means clustering on the sentences.
def cluster_text(k, title_string, load=False)
    new_text = prepare_text(title_string)
    sentences, samples = prepare_samples(new_text)
    unigrams = get_unigrams(new_text)

    kmeans = None

    if not load:
        kmeans = cluster(k, unigrams, samples, title_string)
    else:
        kmeans = load('kmeans_' + title_string + '.joblib')
    labels = kmeans.labels_
    # print(kmeans.inertia_)

    # Display the sizes of the clusters.
    unique, counts = np.unique(labels, return_counts=True)
    cluster_sizes = dict(zip(unique, counts))
    print(cluster_sizes)

    return samples, sentences, labels, cluster_sizes

def compute_transition_matrix(samples, labels):
    # Count the number of transitions from state to state.
    transitions = np.zeros((k, k))
    for i in range(1, len(samples)):
        curr = labels[i]
        prev = labels[i - 1]
        transitions[prev][curr] += 1

    # Compute the probabilities of each kind of transition.
    transitions_normalized = np.array([transitions[0] / cluster_sizes[0]])
    for i in range(1, k):
        add_row = np.array([transitions[i] / cluster_sizes[i]])
        transitions_normalized = np.concatenate((transitions_normalized, add_row))

    transitions_list = transitions_normalized.tolist()

    return transitions_list

# Based on the transition matrix, generate a sequence of labels of length seq_length.
def generate_state_sequence(seq_length, transitions_list):
    gen_sequence = [0]
    prev = gen_sequence[0]
    for i in range(1, seq_length):
        next = random.choices(list(range(k)), weights=transitions_list[prev])[0]
        gen_sequence.append(next)
        prev = next

    return gen_sequence

# Create and train a different Markov chain on each cluster.
def generate_markov_chains(labels, sentences):
    cluster_dict = sort_samples_by_cluster(labels, sentences)
    markov_chains = []

    for key in cluster_dict.keys():
        cluster_continuous = '. '.join(cluster_dict[key])
        text_model = markovify.Text(cluster_continuous, state_size=2)
        markov_chains.append(text_model)

    return markov_chains

# Iterate through the generated label sequence and deploy the
# corresponding Markov model to generate a sentence per label.
# The resulting sequence of sentences should approximate
# a paragraph of prose.
def generate_nice_paragraph(gen_sequence, markov_chains):
    sentence_sequence = []

    for state in gen_sequence:
        state_model = markov_chains[state]
        sentence_sequence.append(text_model.make_sentence())

    return sentence_sequence
    
print(" ".join(sentence_sequence))

narration = cluster_dict[0]
narration_continuous = " ".join([sentence + "." for sentence in narration])

sentences, samples = prepare_samples(narration_continuous)
unigrams = get_unigrams(narration_continuous)
# kmeans = cluster(4, unigrams, samples, "persuasion_narration")
kmeans = load('kmeans_persuasion_narration.joblib')
labels = kmeans.labels_
print(kmeans.inertia_)
unique, counts = np.unique(labels, return_counts=True)
cluster_sizes = dict(zip(unique, counts))
print(cluster_sizes)

cluster_dict = sort_samples_by_cluster(labels, sentences)
show_cluster_sentences(sentences, labels)

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
