from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from nltk.corpus import stopwords
import string
import re
import spacy
from spacy.tokens import Doc


#-------------------------------------------------------------------
# DEFAULT SETTINGS
#-------------------------------------------------------------------

# SPACY NLP MODEL
nlp = spacy.load('en_core_web_sm')

# STOPWORDS TO BE REMOVED
STOPLIST = set(stopwords.words('english') + ["n't", "'s", "'m", "ca"] + list(ENGLISH_STOP_WORDS))

# SYMBOLS TO BE REMOVED
SYMBOLS = " ".join(string.punctuation).split(" ") + ["-----", "---", "...", "“", "”", "'ve"]