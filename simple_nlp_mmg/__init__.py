from sklearn.feature_extraction.text       import CountVectorizer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from sklearn.base     import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm      import LinearSVC
from nltk.corpus      import stopwords
from spacy.tokens     import Doc

import string
import re
import spacy


#-------------------------------------------------------------------
# DEFAULT SETTINGS
#-------------------------------------------------------------------

# SPACY NLP MODEL
nlp = spacy.load('en_core_web_lg')

# STOPWORDS TO BE REMOVED
STOPLIST = set(stopwords.words('english') + ["n't", "'s", "'m", "ca"] + list(ENGLISH_STOP_WORDS))

# SYMBOLS TO BE REMOVED
SYMBOLS = " ".join(string.punctuation).split(" ") + ["-----", "---", "...", "“", "”", "'ve"]

WHITESPACE = ["", " ", "  ", "   ","    ", "\t", "\n", "\r\n", "\n\n"]