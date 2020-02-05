import markovify
import re
import markov_novel

def process(text):
    # remove chapter headings
    new_text = text
    matches = re.findall("CHAPTER \d+|Chapter \d+", text)
    for match in matches:
        new_text = re.sub(match, '', new_text)
    return new_text

# Get raw text as string.
with open("Corpus/Northanger.txt", encoding="utf8") as f:
    northanger_text = f.read()

with open("Corpus/Pride.txt", encoding="utf8") as f:
    pride_text = f.read()

with open("Corpus/Sense.txt", encoding="utf8") as f:
    sense_text = f.read()

combined_text = " ".join([northanger_text, pride_text, sense_text])
    
processed_text = process(combined_text)
# Build the model.
text_model = markovify.Text(processed_text)

# novel = markov_novel.Novel(text_model, chapter_count=5)
# novel.write(novel_title='my-novel', filetype='md')

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(280))