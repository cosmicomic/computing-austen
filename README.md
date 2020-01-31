# computing-austen

A CS 81 project that applies techniques in natural language generation and sentiment analysis to Jane Austen's six novels.

## Aims

1. Generate sentences or passages in the style of Jane Austen by training a generative model or models on the corpus.

   The pipe dream would be to be able to generate Austen-like courtship plots (narrative generation) and then generate Austenian prose to realize those plots -- in effect, computationally "writing an Austen novel". This is probably far beyond the scope of this project and my own time and abilities, but it is perhaps inspiring to keep in mind.

2. Train a classifier that can identify irony in Austen's writing.

   A cool end-product could be some kind of visualization where ironic sentences are highlighted, or sentences are colored with a gradient depending upon an irony score. This would be along the lines of the visualization of the presence of free indirect discourse (FID) in the work of White and Smith.
  
3. Learn more about what is studied in the digital humanities and seek other possible applications of NLP to Jane Austen studies.

## Plan

This section is heavily under development as I do more research on related work and get a better sense of what can be achieved in a project in this domain.

### Current objectives

- Program a simple *n*-gram Markov model (try varying *n*) to produce statistically probable sentences based on the Jane Austen corpus.
  - Texts of the novel are happily available on Project Gutenberg.
- Do more research to get a better sense of future objectives.
  - Read a few articles in the digital humanities.
  - Still have not found work that specifically seeks to emulate the prose writing of a particular author, though I have found a plethora of work on style-constrained poetry generation.
  - Kevin Gilmartin has offered to put me in touch with Ted Underwood, a digital humanist. I should take him up on this.

## Potential future objectives

- Once I have a naive Markov generator working, try to constrain the generated sentences to be grammatically correct.
- As a step towards irony detection, use pre-existing methods to evaluate the valence (positivity/negativity) of passages in Jane Austen.

## Related Work

### Digital Humanities
- Project ["Austen Said"](http://austen.unl.edu/), which uses computational methods to explore patterns in Austen's diction.
- An [overview](http://www.digitalhumanities.org/dhq/vol/11/2/000317/000317.html) of "distant reading".
- ["Literary Pattern Recognition"] (Long and So 2016), a paper that uses ML methods to find statistical patterns in the English haiku.

### Natural Language Generation
- An apparently seminal [paper](https://www.aclweb.org/anthology/W98-1426.pdf) on using *n*-grams for text generation.
- Callaway and Lester, "[Narrative Prose Generation](http://www.sciencedirect.com/science/article/pii/S0004370202002308)" seems to present a process for generating a narrative and the sentences to express it.
- [Song lyrics in the style of Bob Dylan are generated using a Constrained Markov Model, which allows for the control of rhyme and meter](https://www.researchgate.net/publication/236166532_Markov_Constraints_for_Generating_Lyrics_with_Style). 
  - The [PhD thesis](https://pdfs.semanticscholar.org/b71c/7f8888f4dc205daf81ff70d939ac6db86bb8.pdf) of the main author on this paper. Seems to contain potentially useful background information and information on the work itself.
- *The structure of style: algorithmic approaches to understanding manner and meaning* is an entire book on the computational study of style in multiple artistic mediums.

### Sentiment Analysis
- [*SentiArt*](https://www.frontiersin.org/articles/10.3389/frobt.2019.00053/full) is an ML tool that infer the overall emotion ("joyful", "fearful", or "neutral" in the paper) of passages from Harry Potter novels.
