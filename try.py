import markovify
import re
# import markov_novel
# import spacy
import nltk

# nlp = spacy.load('en_core_web_sm')

class NLTKPOSifiedText(markovify.Text):
    def word_split(self, sentence):
        problem_words = []

        words = re.split(self.word_split_pattern, sentence)
        # words = [word for word in words if len(words) > 0]
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

# class SpacyPOSifiedText(markovify.Text):
#     def word_split(self, sentence):
#         return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

#     def word_join(self, words):
#         sentence = " ".join(word.split("::")[0] for word in words)
#         return sentence

def process(text):
    # remove chapter headings
    new_text = text
    matches = re.findall("CHAPTER \d+|Chapter \d+", text)
    for match in matches:
        new_text = re.sub(match, '', new_text)
    return new_text

# Get raw text as string.
# with open("Corpus/Northanger.txt", encoding="utf8") as f:
#     northanger_text = f.read()

# with open("Corpus/Pride.txt", encoding="utf8") as f:
#     pride_text = f.read()

# with open("Corpus/Sense.txt", encoding="utf8") as f:
#     sense_text = f.read()

# combined_text = " ".join([northanger_text, pride_text, sense_text])

# combined_text = northanger_text
    
with open("Corpus/Persuasion.txt", encoding="utf8") as f:
    persuasion_text = f.read()
processed_text = process(persuasion_text)
# processed_text = process(combined_text)
# Build the model.
text_model = markovify.Text(processed_text, state_size=2)
# text_model = SpacyPOSifiedText(processed_text)
# text_model = NLTKPOSifiedText(processed_text, state_size=3)

# novel = markov_novel.Novel(text_model, chapter_count=5)
# novel.write(novel_title='my-novel', filetype='md')
sentence_sequence = []
# Print five randomly-generated sentences
for i in range(8):
    sentence_sequence.append(text_model.make_short_sentence(280))

print(" ".join(sentence_sequence))

# Print three randomly-generated sentences of no more than 280 characters
# for i in range(3):
#     print(text_model.make_short_sentence(280))