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

print(len(all_dialog))
dialog_string = " ".join(all_dialog)
print(len(all_narration))
narration_string = " ".join(all_narration)

seq_dict = {0 : sequence.count(0), 1 : sequence.count(1)}

transition_matrix = compute_transition_matrix(2, sequence, sequence, seq_dict)
print(transition_matrix)

# kmeans, samples, sentences, labels, cluster_sizes = cluster_text_from_string(k, clean_titles(dialog_string))
# print("Dialog Clusters")
# show_cluster_sentences(sentences, labels, num_sample_sentences=8)

# print("Narration Clusters")
# kmeans, samples, sentences, labels, cluster_sizes = cluster_text_from_string(k, clean_titles(narration_string))
# show_cluster_sentences(sentences, labels, num_sample_sentences=8)