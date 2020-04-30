import xml.etree.ElementTree as ET

# tree structure: TEI -> (teiHeader, text)
# text -> body -> div (32)
# div -> n -> (head, )

def extract_said(said, aloud):
    bool_to_str = {True : 'true', False : 'false'}
    if 'aloud' in child.attrib:
        if child.attrib['aloud'] == bool_to_str[aloud]:
            if child.text is not None:
                print(child.text)
            else:
                print(child.attrib)

tree = ET.parse('Corpus/xml/NA.xml')
root = tree.getroot()

body = root[1][0] # has 32 divisions/chapters (Chapter 0 is "advertisement by the authoress")
chap1 = body[1]
chap2 = body[2]

# ps = chap1.findall('{http://www.tei-c.org/ns/1.0}p')
ps = chap2.findall('{http://www.tei-c.org/ns/1.0}p')

for chap in body:
    ps = chap.findall('{http://www.tei-c.org/ns/1.0}p')
    for p in ps:
        for child in p:
            if child.tag == '{http://www.tei-c.org/ns/1.0}said':
                extract_said(child, True)
            elif child.tag == "{http://www.tei-c.org/ns/1.0}seg":
                subsegs = child.findall('{http://www.tei-c.org/ns/1.0}said')
                for sub in subsegs:
                    print("seg")
                    extract_said(sub, True)

# said = chap1[1][0]

# print(said.attrib)
# print(said.text)