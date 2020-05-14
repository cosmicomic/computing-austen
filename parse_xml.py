import xml.etree.ElementTree as ET

import re
from prepare_text import *

# tree structure: TEI -> (teiHeader, text)
# text -> body -> div (32)
# div -> n -> (head, )

k = 4
seq_length = 5

bool_to_str = {True : 'true', False : 'false'}

def extract_said_from_p(said, aloud):
    if 'aloud' in child.attrib:
        if child.attrib['aloud'] == bool_to_str[aloud]:
            if child.text is not None:
                print(child.text)
            else:
                print(child.attrib)

def remove_ws(string):
    return " ".join(string.split())

def remove_qm(string):
    removed_left = string.replace("“", "")
    return removed_left.replace("”", "")

def is_dialog(element):
    return element.attrib['aloud'] == 'true' and element.attrib['direct'] == 'true'


tree = ET.parse('Corpus/xml/NA.xml')
root = tree.getroot()

body = root[1][0] # has 32 divisions/chapters (Chapter 0 is "advertisement by the authoress")
chap1 = body[1]
chap2 = body[2]

# ps = chap1.findall('{http://www.tei-c.org/ns/1.0}p')
ps = chap2.findall('{http://www.tei-c.org/ns/1.0}p')

all_dialog = []
all_narration = []
sequence = []

for chap in body[1:]:
    ps = chap.findall('{http://www.tei-c.org/ns/1.0}p') # find all non-header elements
    for p in ps: # for each non-header element
        for child in p:
            if child.tag == '{http://www.tei-c.org/ns/1.0}said':
                if child.text:
                    clean = remove_qm(remove_ws(child.text))
                    if is_dialog(child):
                        all_dialog.append(clean)
                        sequence.append(1)
                    else:
                        all_narration.append(clean)
                        sequence.append(0)
                else:
                    clean = remove_qm(remove_ws(child[0].tail))
                    if is_dialog(child):
                        all_dialog.append(clean)
                        sequence.append(1)
                    else:
                        all_narration.append(clean)
                        sequence.append(0)
            elif child.tag == "{http://www.tei-c.org/ns/1.0}seg":
                for meow in child:
                    if meow.text:
                        clean = remove_qm(remove_ws(meow.text))
                        if 'aloud' not in meow.attrib:
                            pass
                        else:
                            if is_dialog(meow):
                                all_dialog.append(clean)
                                sequence.append(1)
                            else:
                                all_narration.append(clean)
                                sequence.append(0)
                    else:
                        # NOTE: text with 'certainty' is not direct dialog
                        clean = remove_qm(remove_ws(meow[0].tail))
                        if is_dialog(meow):
                            all_dialog.append(clean)
                            sequence.append(1)
                        else:
                            all_narration.append(clean) 
                            sequence.append(0)

dialog_string = " ".join(all_dialog)
narration_string = " ".join(all_narration)

seq_dict = {0 : sequence.count(0), 1 : sequence.count(1)}

dn_transitions = compute_transition_matrix(2, sequence, sequence, seq_dict)
# print(transition_matrix)

generated_sequence = generate_state_sequence(2, 100, dn_transitions, start=0)
print(generated_sequence)

# kmeans, samples, sentences, labels, cluster_sizes = cluster_text_from_string(k, clean_titles(dialog_string))
# dump([sentences, labels, cluster_sizes], "NA_dialog_output")

# print("Dialog Clusters")
[sentences, labels, cluster_sizes] = load("NA_dialog_output")
dialog_chains = generate_markov_chains(labels, sentences)
dialog_transitions = compute_transition_matrix(k, labels, labels, cluster_sizes)

# show_cluster_sentences(sentences, labels, num_sample_sentences=8)
# sequence = generate_state_sequence(k, seq_length, dialog_transitions)
# print(generate_nice_paragraph(sequence, dialog_chains))

# print("Narration Clusters")
# kmeans, samples, sentences, labels, cluster_sizes = cluster_text_from_string(k, clean_titles(narration_string))
# dump([sentences, labels, cluster_sizes], "NA_narration_output")
[sentences, labels, cluster_sizes] = load("NA_narration_output")
narration_chains = generate_markov_chains(labels, sentences)
narration_transitions = compute_transition_matrix(k, labels, labels, cluster_sizes)

# sequence = generate_state_sequence(k, seq_length, narration_transitions)
# print(generate_nice_paragraph(sequence, narration_chains))
# show_cluster_sentences(sentences, labels, num_sample_sentences=8)

chapter_text = []
i = 1
curr_state = generated_sequence[0]
curr_length = 1
while i < len(generated_sequence):
    if generated_sequence[i] == curr_state:
        curr_length += 1
    else:
        # generate sentence sequence
        if curr_state == 1:
            subsequence = generate_state_sequence(k, curr_length, dialog_transitions)
            addition = generate_nice_paragraph(subsequence, dialog_chains)
            addition = ["“" + x + "”\n" for x in addition]
            addition = ["\n"] + addition
        else:
            subsequence = generate_state_sequence(k, curr_length, narration_transitions)
            addition = generate_nice_paragraph(subsequence, narration_chains)
        chapter_text += addition
        curr_length = 0
        curr_state = generated_sequence[i]

    i += 1

chapter_text_string = " ".join(chapter_text)
f = open("ersatz.txt", "a")
f.write(chapter_text_string)
f.close()

