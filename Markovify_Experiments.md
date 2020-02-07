# Experiments with Markovify
February 6, 2020


## "Methodology"

These experiments were informal and meant to get a first impression of the results from applying Markovify to the corpus. Template code from the Github repository of Markovify was used, generating five sentences with no constraints, followed by three sentences constrained to be under 280 characters. The sentences below are samples of text generated with this simple code. 

Observations were impressionistic, and patterns were not tested statistically. More rigorous testing may follow if it is determined to be worthwhile.

## Varying _n_ with the generic model

Corpus was the text of _Northanger Abbey_. For each _n_, the first sentence is generated with no constraints, while the second is constrained to be 280 characters or less.
### n = 1
* She ventured, when her feel that her thread, if he afford to understand him--and he can afford to show her hand; but observe anything in favour of reading aloud with joyful haste, to the contriver may be greatly discomposed; I believe himself on to stay than those detestable rain.
* “Oh! dear, I suppose but there would rather the violence of not allowed to our seeing you have done completely; not entirely silent; and, in their walking.

### n = 2
* The chaise of a rattle, nor to what had passed away, and I was to produce animosities between the other had, in all their diversities, without having discerned even an antique chimney.
* I wish I had much rather take a turn with her till Tuesday.

### n = 3
* She resolved on not answering Isabella's letter, and tried to turn it; but it resisted her utmost strength.
* The hope of meeting again in the fullness of privileged affection.

### Observations
As _n_ increases, the sentences go from barely coherent to more grammatical and meaningful. This is expected, as widening the "horizon" of the model captures more of the grammatical structure of the language. 

Something also to note is that there are opening/closing quotes without corresponding closing/opening quotes. This makes sense given that I have not tried to __distinguish dialog from narration or impose any rule for well-formed quotations__. A more sophisticated approach would be to have separate generative models for dialog vs. narration. The ratio of dialog to narration would also need to be estimated, and templates for dialog (e.g. "<dialog>, <character> said") could be imposed.

## Including multiple novels in the corpus
These sentences were generated from corpus consisting of _Northanger Abbey_, _Sense and Sensibility_, and _Pride and Prejudice_, which are Austen's earliest written published novels.

### n = 2
* “Lady Catherine, I quite envy you; but make haste and get a good kind of pride and obsequiousness, self-importance and humility.
* “Undoubtedly,” replied Darcy, “was to show them every respect.
* Mr. Morland would not hear above one word from you as you can, and then we may have been.

### n = 3
* No, he had been so obstinate, Catherine,” said James; “you were not used to your odd ways.”
* Mr. Collins and Charlotte were both standing at the gate to hear and satisfy his inquiries after all her family.
* “Oh! dear, there are a great many pretty women in the world--especially of those--whoever they may be--with whom I happen to be in fact perfectly safe, and therefore would alarm herself no longer.

### Observations
There were some sentences in which characters from different novels appeared to be interacting with one another. However, it was more likely for characters from the same novel to be mentioned in a single sentence, probably because such characters were mentioned together in the original text. 

Also, __sentences that appeared to draw more from _Pride and Prejudice_ (i.e. mention characters from that novel) dominated in frequency__. This can partly be understood by the fact that _Pride and Prejudice_, at 120,697 words is the longest of the three novels. But while it is much longer than _Northanger Abbey_ (77, 815 words), it is not much longer than _Sense and Sensibility_ (119,394 words). (Word counts were taken from the following source: https://www.janetogeorgette.com/word-counts-for-your-favourite-regency-romance-novels/)

There are two explanations that come to mind. One is that _Pride and Prejudice_ has a more complex network of characters, and/or that it simply mentions the names of characters more frequently than do the other two novels. The former seems true to me, as, for example, there are five Bennett sisters, as opposed to the two Dashwood sisters in _Sense_ and just Catherine in _Northanger_. This might be worth looking into.

## Using part-of-speech tagging to generate more grammatical sentences

The Markovify README gives examples of using part-of-speech taggers from NLTK and Spacy. These were fairly easy to deploy, though the Spacy tagger ironically led to the creation of sentences with erratic spacing. Thus, only sentences generated using NLTK tagging are presented below.

### n = 2
* Mr. Bennet say voluntarily to subjects which her sister by her cousin by the fire place, and his taste delicate and pure.
* Belle went with her; and when at Barton.
* Catherine was left to the ground; and Margaret, by being told that she might have seen how well she might, for the entail, I should be the meaning of this?
* “I know little of the chest in undisputed possession!
* Jane shook her head from every wish of exploring them after dinner, and then I found there would be soon increased by noise.

### n = 3

* Elizabeth had frequently united with Jane in the scheme, and as, with such a companion at Brighton, where the temptations must be greater than at home.
* But on Wednesday, I think, Henry, you may expect us; and we shall very soon settle it with her, I am not so selfish, however, as to press for it, if inconvenient.
* Don't fancy that you will not tell me.”
* She and your brother choose to go, and you will feel the effects of your loveliness and amiable qualifications.
* Her wretchedness I could have an opportunity of exhibiting was delightful to be really in an abbey.

### Observations

It is hard to say if these sentences are more grammatical than the sentences generated with the generic model. In fact, they seem to make less sense than the generically generated sentences, and they also feel less recognizably Austenian. I would guess that this is because the structures of the original sentences have been broken apart by whatever template the part-of-speech processor is using to construct "more grammatical" sentences.

__In terms of computational creativity, the loss of original structure may be a good thing, as it seems more conducive to the creation of new meaning than does the purely statistical approach.__

## Summary

* Varying _n_ had the expected results.
* To generate more "realistic" text, dialog should be distinguished from narration.
* The dominance of _Pride and Prejudice_ characters in the generated sentences may reflect the larger number of characters in the novel compared to the other two.
* Imposing part-of-speech tagging and templates (which are pretty coarse, since I used them out of the box) gives mixed results in terms of generating grammatical sentences.  But, using the template structure in place of the original sentence structure seems to have a greater potential to create new meaning than otherwise.