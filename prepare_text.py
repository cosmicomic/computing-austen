import re
import string

with open("Corpus/Northanger excerpt.txt", encoding="utf8") as f:
    northanger_text = f.read()

# remove chapter headings
new_text = northanger_text
matches = re.findall("CHAPTER \d+|Chapter \d+", northanger_text)
for match in matches:
    new_text = re.sub(match, '', new_text)

# compile set of bigrams
words = re.split(r'\W+', new_text)
words = [word.lower() for word in words if word != ""]
print(words[:100])

bigrams = []

for i in range(len(words) - 1):
    bigrams.append((words[i], words[i + 1]))

bigrams = list(set(bigrams))

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

bigram_sets = []

# convert sentences into sets of bigrams
for sentence in remove_punct:
    tokenized_sentence = re.split(r'\W+', sentence)
    

# with open('northanger_processed.txt', 'w', encoding="utf-8") as f:
#     for sentence in remove_newlines:
#         f.write(sentence + ".\n")