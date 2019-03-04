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
import regex as re


re.DEFAULT_VERSION = re.VERSION1
split_chars = lambda char: list(char.strip().split(' '))
#-------------------------------------------------------------------
# DEFAULT SETTINGS
#-------------------------------------------------------------------

# SPACY NLP MODEL
nlp = spacy.load('en_core_web_sm')

#--------------------------------------------------------------------
# STOPWORDS TO BE REMOVED
#--------------------------------------------------------------------
STOPLIST = set(stopwords.words('english') + ["n't", "'s", "'m", "ca"] + list(ENGLISH_STOP_WORDS))

#--------------------------------------------------------------------
# SYMBOLS TO BE REMOVED
#--------------------------------------------------------------------
SYMBOLS = " ".join(string.punctuation).split(" ") + ["-----", "---", "...", "“", "”", "'ve"]

#--------------------------------------------------------------------
# CAPTURE WHITESPACE CHARACTERS
#--------------------------------------------------------------------
WHITESPACE = ["", " ", "  ", "   ","    ", "\t", "\n", "\r\n", "\n\n"]

#--------------------------------------------------------------------
# WORDS THAT MEAN NUMBERS
#--------------------------------------------------------------------
NUM_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
              'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
              'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
              'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
              'hundred', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
              'gajillion', 'bazillion']

#--------------------------------------------------------------------
# UNTIS
#--------------------------------------------------------------------
_units = ('km km² km³ m m² m³ dm dm² dm³ cm cm² cm³ mm mm² mm³ ha µm nm yd in ft '
          'kg g mg µg t lb oz m/s km/h kmh mph hPa Pa mbar mb MB kb KB gb GB tb '
          'TB T G M K % км км² км³ м м² м³ дм дм² дм³ см см² см³ мм мм² мм³ нм '
          'кг г мг м/с км/ч кПа Па мбар Кб КБ кб Мб МБ мб Гб ГБ гб Тб ТБ тб'
          'كم كم² كم³ م م² م³ سم سم² سم³ مم مم² مم³ كم غرام جرام جم كغ ملغ كوب اكواب')
UNITS  = split_chars(_units)

#--------------------------------------------------------------------
# CURRENCY
#--------------------------------------------------------------------
_currency = r'\$ £ € ¥ ฿ US\$ C\$ A\$ ₽ ﷼ ₴'
CURRENCY  = split_chars(_currency)

#--------------------------------------------------------------------
# PUNCTUATION
#--------------------------------------------------------------------
_punct = r'… …… , : ; \! \? ¿ ؟ ¡ \( \) \[ \] \{ \} < > _ # \* & 。 ？ ！ ， 、 ； ： ～ · । ، ؛ ٪'
PUNCT  = split_chars(_punct)

#--------------------------------------------------------------------
# QUOTES
#--------------------------------------------------------------------
_quotes = r'\' \'\' " ” “ `` ` ‘ ´ ‘‘ ’’ ‚ , „ » « 「 」 『 』 （ ） 〔 〕 【 】 《 》 〈 〉'
QUOTES  = split_chars(_quotes)

#--------------------------------------------------------------------
# HYPHENS
#--------------------------------------------------------------------
_hyphens = '- – — -- --- —— ~'
HYPHENS  = split_chars(_hyphens)

#--------------------------------------------------------------------
# ICONS
#--------------------------------------------------------------------
_other_symbols = r'[\p{So}]'
ICONS  = [_other_symbols]








