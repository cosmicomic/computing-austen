import re
from prepare_text import *

k = 4
seq_length = 5

text = prepare_text("Persuasion")
dialog_pattern = r'\"([^\"]+?)(\"|\-\-\n)'

talk = re.findall(dialog_pattern, text)

dialog = ""

# for t in talk:
#     print(re.sub('\n', ' ', t[0]))

for t in talk:
    dialog += t[0] + '\n'

# with open("Corpus/PersuasionDialog.txt", "w", encoding="utf8") as f:
#     f.write(dialog)

narration = re.sub(dialog_pattern, '', text)

with open("Corpus/PersuasionNarration.txt", "w", encoding="utf8") as f:
    f.write(narration)

text_string = narration
# text_string = dialog

### Make a fresh clustering
# kmeans, samples, sentences, labels, cluster_sizes = cluster_text_from_string(k, text_string)
# dump(kmeans, 'kmeans_' + 'PersuasionNarration' + '.joblib') 
# dump(kmeans, 'kmeans_' + 'PersuasionDialog' + '.joblib') 

### Load previous clustering
samples, sentences, labels, cluster_sizes = cluster_text_from_file(k, 'PersuasionNarration', saved=True)
show_cluster_sentences(sentences, labels, num_sample_sentences=5)

transitions_list = compute_transition_matrix(k, samples, labels, cluster_sizes)

gen_sequence = generate_state_sequence(k, seq_length, transitions_list)
markov_chains = generate_markov_chains(labels, sentences)
print(gen_sequence)
sentence_sequence = generate_nice_paragraph(gen_sequence, markov_chains)
print(" ".join(sentence_sequence))