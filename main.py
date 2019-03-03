# import the 
from simple_nlp_mmg.simple_nlp import simple_nlp

#-------------------------------------------------------------------------
# Importing Text
#-------------------------------------------------------------------------
f    = open('data/example.txt')
text = f.read()
snlp = simple_nlp(text)

#-------------------------------------------------------------------------
# Process the text
#-------------------------------------------------------------------------
snlp.process()
print(snlp.features)





