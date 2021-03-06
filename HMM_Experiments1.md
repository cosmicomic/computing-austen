# Initial Experiments with HMMs

February 21, 2020

## Method

This method is suited primarily for modeling the structure and content of _domain-specific_ texts. When I implemented it as a teenager, I used it to model dialogs between a user and an AI that could answer questions about bus schedules. The same fundamental method has been used in research on generating and summarizing reports of earthquakes and news stories about specific topics such as drugs, finance, and accidents (Barzilay and Lee, 2004). The overall idea is to model topics as the hidden states of the HMM and units (n-grams) of the text or dialog as the observations emitted by the states. 

The first step of the process I used in my previous project was to infer topics by _k_-clustering utterances based on unigram (word) frequencies. This would give us an initial estimate of the emission probability matrix, which gave the probabilities of utterances being emitted by certain states. If _N_ is the size of the vocabulary in the corpus, each utterance would be represented as an _N_-vector, with a 1 at index _i_ if the utterance contains the word indexed with _i_ and 0 otherwise. Because the AI used fairly limited language, certain utterances were highly correlated, so clustering was good.

From these initial state assignments, state transition  and observation probability matrices could be computed. The Viterbi algorithm was then used to re-estimate the parameters of the model.

## Application to _Northanger Abbey_

In trying to apply the above method to this project, I ran into problems in the clustering step. In the previous project, I had used the presence or absence of certain unigrams as features for the vectors. But in this case, in which I am trying to generate text, unigrams are not appropriate because they tend not to generate very coherent text. Some evidence is that the text I generated using a [pre-existing HMM text generator](https://github.com/mfilej/nlg-with-hmmlearn) was worse gibberish than that generated by the unigram Markov chain.

I implemented the clustering procedure using bigrams instead, which was the approach of Barzilay and Lee. But this also turned out to be problematic. The language of a novel, particularly an 18th/19th century novel, tends to be highly rich and varied, so bigrams tend not to repeat themselves much, making it hard to cluster sentences based on shared bigrams. 

Linguistic repetitiveness is an important assumption of Barzilay and Lee's work:

"Of course, the success of the distributional approach
depends on the **existence of recurrent patterns**. In arbitrary
document collections, such patterns might be too
variable to be easily detected by statistical means. However,
research has shown that texts from the same domain
tend to exhibit high similarity (Wray, 2002). Cognitive
psychologists have long posited that this similarity is not
accidental, arguing that **formulaic text structure** facilitates
readers’ comprehension and recall (Bartlett, 1932)."

And a good novel is anything but formulaic. 

As expected, the clusters seemed not to be very meaningful. The distribution of clusters when _k = 3_ was {0: 1, 1: 477, 2: 3475}, and the distribution when _k = 4_ was {0: 341, 1: 1, 2: 3610, 3: 1}. Thus, there were basically two clusters, and one contained the overwhelming majority of sentences. 

My sense is that the clusters are unlikely to be well-defined. If they were, then this result would suggest that there are basically two kinds of sentences in _Northanger Abbey_. But sentences in the novel (and any novel) are highly varied, which suggests that the clusters are probably very spread out and thus not meaningful.