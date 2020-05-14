# computing-austen

A CS 81 project that applies techniques in natural language generation and sentiment analysis to Jane Austen's six novels.

## Aims

1. Generate sentences or passages in the style of Jane Austen by training a generative model or models on the corpus.

   The pipe dream would be to be able to generate Austen-like courtship plots (narrative generation) and then generate Austenian prose to realize those plots -- in effect, computationally "writing an Austen novel" (or at least short story). This is probably far beyond the scope of this project and my own time and abilities, but it is perhaps inspiring to keep in mind.

2. Train a classifier that can identify irony in Austen's writing.

   A cool end-product could be some kind of visualization where ironic sentences are highlighted, or sentences are colored with a gradient depending upon an irony score. This would be along the lines of the visualization of the presence of free indirect discourse (FID) in the work of White and Smith.
  
3. Learn more about what is studied in the digital humanities and seek other possible applications of NLP to Jane Austen studies.

## Plan ##

This section is heavily under development as I do more research on related work and get a better sense of what can be achieved in a project in this domain.

### Update (5/13) ###
This week, I basically figured out how to parse the XML files, at least for *Northanger Abbey*, allowing me to create an ersatz chapter, which you can read [here](https://github.com/cosmicomic/computing-austen/blob/master/The%20walls%20were%20papered.pdf).

#### Highlights ####
My algorithm seemed to have generated some pretty existential prose, which reminded me of Virginia Woolf's *To the Lighthouse* (which is one of my favorite novels) and other modernist works.

- "The anxieties of common life began soon to succeed to the window, fidgeted about, hummed a tune, and seemed wholly self-occupied."
- Catherine, recollecting herself, grew ashamed of having explained them. 
 “Yes, but you forget that your mother died.”
- "They were viewing the country with the common feelings of common life, than with the same hand, marked an expenditure scarcely more interesting, in letters, hair-powder, shoe-string, and breeches-ball."

#### Process ####

The process for doing this was somewhat complicated and grungy. Here is an explanation: 

- I was able to separate dialog from narration pretty cleanly, which allowed me to create a 2-state Markov chain to model transitions between dialog and narration. 
- Using code I wrote earlier in the project, I ran clustering on dialog and narration separately, obtaining Markov chains corresponding to dialog clusters and narration clusters. 
	- I also computed state transition probability matrices for dialog and narration. 
- Then, I generated a probable sequence of narration and dialog based on the higher-order 2-state Markov chain. I set the length of the sequence to be 100 sentences, to approximate a chapter. 
	- For each continuous block of *n* sentences of narration or dialog, I pretended I was generating a paragraph of length *n* of narration or dialog, respectively. I used my earlier process of generating a probable state sequence of length *n* based on a state transition probability matrix. Then, for each state, I had the corresponding Markov chain generate a sentence.
	- In order to make the dialog look more like dialog, I surrounded each dialog sentence with quotation marks and put it on a new line.
- Finally, I took the entire generated text, pasted it into a Word document, and manually formatted it by indenting each line of dialog and the beginning of each paragraph.

For completeness, I want to generate fake chapters for Austen's other five novels. After that, I could try to write a more refined procedure for generating conversations specifically.

### Update (4/29) ###

- Found marked-up XML files of the novels from a source I had actually found at the start of this project, "Austen Said". The XML files can be found [here](http://austen.unl.edu/about#download).
	- They are in a very particular format, as specified by the [TEI](https://tei-c.org/Guidelines/P5/), which is an organization that maintains guidelines for encoding digital humanities texts.
	- Mostly spent this week figuring out how to parse this text and extract what I need. These efforts will continue into the next week.

### Update (4/23) ###

- Separated dialog from narration, and ran clustering on and generated paragraphs from each separately
	- Results seem to be nicer than before, as first-person and third-person are no longer wildly mixed in the same paragraph
	- Unsurprisingly, "narration paragraphs" are much longer than "dialog paragraphs". Surprisingly, the narration paragraphs are not that much less believable than the dialog paragraphs.
	- With these results, it feels like I could generate a sort of "statistical approximation" of the novel, by calculating the ratio of narration to dialog, generating narrative and dialog sentences accordingly, and putting them all together. Not sure if this is worth doing.
- I am more interested in simulating conversations. At this point it may be a good idea to start grouping dialog manually. 
	- Although I could use regular expressions to separate dialog and narration, it was very coarse: basically every bit of text surrounded by quotation marks in the novel got mashed together (separated only by spaces and periods) into one huge dialog unit. Also, the separation was not perfect.
	- I may just go through each conversation in the novel manually and create a corpus where pieces of dialog are grouped by whether or not they're in the same conversation.
- Further down the line, it might be cool to see if I could use a pre-existing supervised learning algorithm (e.g. for sentiment analysis) to measure irony in Austen sentences. This would also require manually marking sentences, on a subjective irony scale.


### Update (3/6)
- I rethought my approach last week and tried again in a smarter (I think) way. The idea is still to use the HMM/clustering to infer topics, but to have a different Markov chain for each topic to generate sentences based on a probabilistically generated sequence of topics. Write-up here: https://github.com/cosmicomic/computing-austen/blob/master/Clustering.md
  - I didn't actually finish the HMM since the clustering yielded interesting results on its own. Completing the HMM modeling could be a good way to spend the next week to see if it generates even more natural sounding paragraphs, though there may be some computational difficulties (the probabilities involved would be vanishingly small, I think). Another route might be to focus on dialogue and try to simulate Austenian conversations. The simulated conversations could then be integrated into some generated narration. This would address the current issue of the generated language indiscriminately mixing the narrator's voice with the characters' speech.

### Weekly Update (2/8-2/21)
- Progress was slow these past two weeks due to some health issues.
- Worked on trying to use an HMM as a generative model to see if it would do any better than a Markov chain. My hypothesis, based on a project I did back in high school at Microsoft Research, was that it might impose more structure on the generated text. The initial results have been poor. See [HMM_Experiments1.md](https://github.com/cosmicomic/computing-austen/blob/master/HMM_Experiments1.md) for a write-up.
  - Using [pre-existing code](https://github.com/mfilej/nlg-with-hmmlearn) generated gibberish worse than the unigram Markov chain. I decided to write my own code from scratch (relatively).
  - Revisited an old write-up of the project I did in high school. It turned out that the approach I had used back then was not suited to the present task because the language that Austen uses is obviously much richer and more variable than that of an AI that answers questions about bus schedules, or [reports about earthquakes](https://www.aclweb.org/anthology/N04-1015/). Indeed, the first step to setting up the model, which is to infer topics by k-clustering observations/utterances, was unsuccessful (the clusters were poor).
- A few options at this point:
  - Use a different approach using HMMs that would be more suited to the task. Some Googling has shown that there was a CS 155 assignment where HMMs were used to generate Shakespeare sonnets. 
  - Abandon HMMs and try to use RNNs, which have also been used to generate Shakespeare sonnets.
  
### Weekly Update (1/31-2/7)

- Used [Markovify](https://github.com/jsvine/markovify/), a Markov chain generator package, to do some basic experiments on the first three Jane Austen novels. See [Markovify_Experiments.md](https://github.com/cosmicomic/computing-austen/blob/master/Markovify_Experiments.md) for a write-up.
- Fell down a rabbit hole trying to do research to get a better sense of future objectives.
  - Read an article by Underwood, "A Geneaology of Distant Reading". He argues that, in literary studies, computational methods are better suited for social and historical questions concerning large numbers of texts, as opposed to New Critical-type questions at the level of single authors. It seems, then, that if I want to accomplish something useful in digital humanities, focusing on Jane Austen is not the right way to go. Prof. Gilmartin noted that one of his research interests is 18th and 19th century periodicals, which there are obviously a lot of. This would be a possible direction if I want to abandon Austen (I don't, yet).
  - Read the journal article on the study of free indirect discourse using the "Austen Said" tool, and learned that computation was used minimally (basically just for word frequency counts). The FID visualizations were created by manually reviewing each sentence and scoring it on intensity in FID.
  - Found a bunch of papers on narrative generation, which involves several stages. Roughly, in narratology, there is a distinction between the creation of the "story world" (_fabula_) vs. the discourse (_syuzhet_) in which that story is realized. A lot of the work under the heading of "computational storytelling" has been done on the former, to the neglect of the latter. There is only one notable exception, which plots a story and then executes it fully, in [Callaway and Lester](http://www.sciencedirect.com/science/article/pii/S0004370202002308).
  - Generating texts with style is basically its own subfield in NLG, which is a subfield of NLP, and there are books and papers written on this topic, which I have compiled in the Zotero for this project (see Related Work).
- Still need to contact people noted below. Delay has mostly been because my goals for this project feel so undefined, though talking to people may help to better define my goals.

### Current objectives

- Look into the Shakespeare sonnets assignment from CS 155, which uses HMMs to generate sonnets.
- Read about RNNs and try to use them as a generative model for this project.
  - Text generation with an RNN using TensorFlow: https://www.tensorflow.org/tutorials/text/text_generation
- Do more research to get a better sense of future objectives.
  - Read a few articles in the digital humanities.
  - Still have not found work that specifically seeks to emulate the prose writing of a particular author, though I have found a plethora of work on style-constrained poetry generation.
- Possibly get in touch with experts. If so, prepare questions, etc.
  - Kevin Gilmartin has offered to put me in touch with Ted Underwood, a digital humanist. I might want to take him up on this.
  - Instructor for Caltech's one-time computational literature class.

## Potential future objectives

- Continue with the Markov approach and introduce structure to the generated text using k-clustering (to infer topics in the text) and a Hidden Markov Model, where the topics are states.
- Try other models that may arrive at grammatical correctness or other desirable features through other means.
- As a step towards irony detection, use pre-existing methods to evaluate the valence (positivity/negativity) of passages in Jane Austen.

## Related Work/Resources

[Zotero](https://www.zotero.org/cosmicomic/items/)

### Corpus
Texts of the novel are happily available on Project Gutenberg.
- [Northanger Abbey](http://www.gutenberg.org/files/121/121-0.txt)
- [Sense and Sensibility](http://www.gutenberg.org/cache/epub/161/pg161.txt)
- [Pride and Prejudice](http://www.gutenberg.org/files/1342/1342-0.txt)
- [Mansfield Park](http://www.gutenberg.org/files/141/141-0.txt)
- [Emma](http://www.gutenberg.org/files/158/158-0.txt)
- [Persuasion](http://www.gutenberg.org/cache/epub/105/pg105.txt)

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
