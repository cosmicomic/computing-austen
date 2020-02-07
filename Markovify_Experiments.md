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

Also, sentences that appeared to draw more from _Pride and Prejudice_ dominated in frequency. This can partly be understood by the fact that _Pride and Prejudice_, at 120,697 words is the longest of the three novels. But while it is much longer than _Northanger Abbey_ (77, 815 words), it is not much longer than _Sense and Sensibility_ (119,394 words). (Word counts were taken from the following source: https://www.janetogeorgette.com/word-counts-for-your-favourite-regency-romance-novels/)

There are two explanations that come to mind. One is that _Pride and Prejudice_ has a more complex network of characters, and/or that it simply mentions the names of characters more frequently than do the other two novels. The former seems true to me, as, for example, there are five Bennett sisters, as opposed to the two Dashwood sisters in _Sense_ and just Catherine in _Northanger_. 

## Using part-of-speech tagging to generate more grammatical sentences