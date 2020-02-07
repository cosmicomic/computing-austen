﻿# computing-austen

A CS 81 project that applies techniques in natural language generation and sentiment analysis to Jane Austen's six novels.

## Aims

1. Generate sentences or passages in the style of Jane Austen by training a generative model or models on the corpus.

   The pipe dream would be to be able to generate Austen-like courtship plots (narrative generation) and then generate Austenian prose to realize those plots -- in effect, computationally "writing an Austen novel" (or at least short story). This is probably far beyond the scope of this project and my own time and abilities, but it is perhaps inspiring to keep in mind.

2. Train a classifier that can identify irony in Austen's writing.

   A cool end-product could be some kind of visualization where ironic sentences are highlighted, or sentences are colored with a gradient depending upon an irony score. This would be along the lines of the visualization of the presence of free indirect discourse (FID) in the work of White and Smith.
  
3. Learn more about what is studied in the digital humanities and seek other possible applications of NLP to Jane Austen studies.

## Plan

This section is heavily under development as I do more research on related work and get a better sense of what can be achieved in a project in this domain.

### Weekly Update (1/31-2/7)

- Used [Markovify](https://github.com/jsvine/markovify/), a Markov chain generator package, to do some basic experiments on the first three Jane Austen novels. See [Markovify_Experiments.md](https://github.com/cosmicomic/computing-austen/blob/master/Markovify_Experiments.md) for a write-up.
- Fell down a rabbit hole trying to do research to get a better sense of future objectives.
  - Read an article by Underwood, "A Geneaology of Distant Reading". He argues that, in literary studies, computational methods are better suited for social and historical questions concerning large numbers of texts, as opposed to New Critical-type questions at the level of single authors. It seems, then, that if I want to accomplish something useful in digital humanities, focusing on Jane Austen is not the right way to go. Prof. Gilmartin noted that one of his research interests is 18th and 19th century periodicals, which there are obviously a lot of. This would be a possible direction if I want to abandon Austen (I don't, yet).
  - Read the journal article on the study of free indirect discourse using the "Austen Said" tool, and learned that computation was used minimally (basically just for word frequency counts). The FID visualizations were created by manually reviewing each sentence and scoring it on intensity in FID.
  - Found a bunch of papers on narrative generation, which involves several stages. Roughly, in narratology, there is a distinction between the creation of the "story world" vs. the discourse (language) in which that story is realized. A lot of the work under the heading of "computational storytelling" has been done on the former, to the neglect of the latter. There is only one notable exception, which plots a story and then executes it fully, in [Callaway and Lester](http://www.sciencedirect.com/science/article/pii/S0004370202002308).
  - Generating texts with style is basically its own subfield in NLG, which is a subfield of NLP, and there are books and papers written on this topic, which I have compiled in the Zotero for this project (see Related Work).
- Still need to contact people noted below. Delay has mostly been because my goals for this project feel so undefined, though talking to people may help to better define my goals.

### Current objectives

- Program a simple *n*-gram Markov model (try varying *n*) to produce statistically probable sentences based on the Jane Austen corpus.
  - Texts of the novel are happily available on Project Gutenberg.
    - [Northanger Abbey](http://www.gutenberg.org/files/121/121-0.txt)
    - [Sense and Sensibility](http://www.gutenberg.org/cache/epub/161/pg161.txt)
    - [Pride and Prejudice](http://www.gutenberg.org/files/1342/1342-0.txt)
    - [Mansfield Park](http://www.gutenberg.org/files/141/141-0.txt)
    - [Emma](http://www.gutenberg.org/files/158/158-0.txt)
    - [Persuasion](http://www.gutenberg.org/cache/epub/105/pg105.txt)
- Do more research to get a better sense of future objectives.
  - Read a few articles in the digital humanities.
  - Still have not found work that specifically seeks to emulate the prose writing of a particular author, though I have found a plethora of work on style-constrained poetry generation.
- Possibly get in touch with experts. If so, prepare questions, etc.
  - Kevin Gilmartin has offered to put me in touch with Ted Underwood, a digital humanist. I might want to take him up on this.
  - Instructor for Caltech's one-time computational literature class.

## Potential future objectives

- Try other models that may arrive at grammatical correctness or other desirable features through other means.
- As a step towards irony detection, use pre-existing methods to evaluate the valence (positivity/negativity) of passages in Jane Austen.

## Related Work

[Zotero](https://www.zotero.org/cosmicomic/items/)

### Digital Humanities
- An [overview](http://www.digitalhumanities.org/dhq/vol/11/2/000317/000317.html) of "distant reading".
- ["Literary Pattern Recognition"](https://lucian.uchicago.edu/blogs/literarynetworks/files/2015/12/LONG_SO_CI.pdf), a paper that uses ML methods to find statistical patterns in the English haiku (start at pg. 17).
- Project ["Austen Said"](http://austen.unl.edu/), which uses computational methods to explore patterns in Austen's diction.
  - This [paper](http://jasna.org/publications/persuasions-online/vol37no1/white-smith/) describes some of the difficulties in tagging textual features that have a subjective component. In their case it is free indirect discourse; in mine, it is irony. 

### Natural Language Generation
- An apparently seminal [paper](https://www.aclweb.org/anthology/W98-1426.pdf) on using *n*-grams for text generation.
- Callaway and Lester, "[Narrative Prose Generation](http://www.sciencedirect.com/science/article/pii/S0004370202002308)" seems to present a process for generating a narrative and the sentences to express it.
- [Song lyrics in the style of Bob Dylan are generated using a Constrained Markov Model, which allows for the control of rhyme and meter](https://www.researchgate.net/publication/236166532_Markov_Constraints_for_Generating_Lyrics_with_Style). 
  - The [PhD thesis](https://pdfs.semanticscholar.org/b71c/7f8888f4dc205daf81ff70d939ac6db86bb8.pdf) of the main author on this paper. Seems to contain potentially useful background information and information on the work itself.
- *The structure of style: algorithmic approaches to understanding manner and meaning* is an entire book on the computational study of style in multiple artistic mediums.

### Sentiment Analysis
- [*SentiArt*](https://www.frontiersin.org/articles/10.3389/frobt.2019.00053/full) is an ML tool that infer the overall emotion ("joyful", "fearful", or "neutral" in the paper) of passages from Harry Potter novels.
