# pip install spacy
# python -m spacy download en_core_web_sm

import spacy
from spacy.tokens import Doc

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en_core_web_sm')
print('-----------------------------------------------------------------')

#-------------------------------------------------------------------------
# Importing Text
#-------------------------------------------------------------------------

text = u'There was once a little boy named Ben, that liked to play with fire. His mother told him that fire was dangerous, so he decided that he would buy a box of matches and head to the lake. As an extra precaution, he swam to the bottom of the lake and lit a fire. There he met a fish who has cold and sat beside him at the bottom of the lake. The fished asked the boy "how did you light a fire underwater?" to which the boy responded "How would a fish know what fire looks like?". "The stars are on fire" said the fish, "and from my home in the lake, I can see the stars at night". "Now how would you know that stars are on fire?" said the boy. "In the same way that you know I am fish" relplied the fish.' 

# Transform the text into a Spacy object

doc = nlp(text)
sents = list(doc.sents)
print('The document:', doc)
print('The sentences:', sents)
print(doc.sentiment)


print('-----------------------------------------------------------------')
#-------------------------------------------------------------------------
# Getting Words and Characters from Documents
#-------------------------------------------------------------------------

# These spacy objects have several interesting properties 
# For instance, you can access the various words in the
# document using their index.
print('The last word          :', doc[-1].text)
print('First Three Words      :', doc[0:3].text)
print('The first 11 characters:', doc[:].text[0:11])
print('The First sentence     :', sents[0])
print('The First word in the second sentence :', sents[1][0])

print('-----------------------------------------------------------------')

#-------------------------------------------------------------------------
# Specify Custom Functions to check for tokens. 
#-------------------------------------------------------------------------
fish_getter = lambda doc: any(token in doc.text for token in ('fish', 'whale', 'shark'))
Doc.set_extension('has_fish', getter=fish_getter)

A = nlp(u'The fish went to the forest for a nap.')
B = nlp(u'The bear went to the forest for a nap.')

print('Document A:', A)
print('Document B:', B)

print('Document A contains fishy terms:',A._.has_fish)
print('Document B contains fishy terms:',B._.has_fish)
print('-----------------------------------------------------------------')

#-------------------------------------------------------------------------
# Check for similarities (higher is more similar)
#-------------------------------------------------------------------------
A = nlp(u"My favorite food is watermellon")
B = nlp(u"a million cup of water grows a pound of food")
similarity = A.similarity(B)

print('Document A:', A)
print('Document B:', B)

print('Similarity between documents A and B:', similarity)
print('-----------------------------------------------------------------')

#-------------------------------------------------------------------------
# Tags of the words
#-------------------------------------------------------------------------
for word in doc:
    print('[Text = ', word.text, '][Tag = ', word.tag_, '][Tag meaning = ', spacy.explain(word.tag_), ']')

#-------------------------------------------------------------------------
# Find named entities, phrases and concepts
#-------------------------------------------------------------------------
for entity in doc.ents:
    print(entity.text, entity.label_)

#-------------------------------------------------------------------------
# Find Nouns in the document
#-------------------------------------------------------------------------
for noun in doc.noun_chunks:
    print(noun.text, 'NOUN')

#-------------------------------------------------------------------------
# Find Nouns in the document
#-------------------------------------------------------------------------
for noun in doc.noun_chunks:
    print(noun.text, 'NOUN')

