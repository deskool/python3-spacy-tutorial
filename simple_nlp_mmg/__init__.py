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
# UNTIS, CURRENCY, QUOTES, PUNCT, HYPHENS, ELLIPSES, ICONS
#--------------------------------------------------------------------
re.DEFAULT_VERSION = re.VERSION1
merge_char_classes = lambda classes: '[{}]'.format('||'.join(classes))
split_chars = lambda char: list(char.strip().split(' '))
merge_chars = lambda char: char.strip().replace(' ', '|')

_bengali         = r'[\p{L}&&\p{Bengali}]'
_hebrew          = r'[\p{L}&&\p{Hebrew}]'
_latin_lower     = r'[\p{Ll}&&\p{Latin}]'
_latin_upper     = r'[\p{Lu}&&\p{Latin}]'
_latin           = r'[[\p{Ll}||\p{Lu}]&&\p{Latin}]'
_persian         = r'[\p{L}&&\p{Arabic}]'
_russian_lower   = r'[ёа-я]'
_russian_upper   = r'[ЁА-Я]'
_sinhala         = r'[\p{L}&&\p{Sinhala}]'
_tatar_lower     = r'[әөүҗңһ]'
_tatar_upper     = r'[ӘӨҮҖҢҺ]'
_greek_lower     = r'[α-ωάέίόώήύ]'
_greek_upper     = r'[Α-ΩΆΈΊΌΏΉΎ]'
_ukrainian_lower = r'[а-щюяіїєґ]'
_ukrainian_upper = r'[А-ЩЮЯІЇЄҐ]'

_upper = [_latin_upper, _russian_upper, _tatar_upper, _greek_upper, _ukrainian_upper]
_lower = [_latin_lower, _russian_lower, _tatar_lower, _greek_lower, _ukrainian_lower]
_uncased = [_bengali, _hebrew, _persian, _sinhala]

ALPHA       = merge_char_classes(_upper + _lower + _uncased)
ALPHA_LOWER = merge_char_classes(_lower + _uncased)
ALPHA_UPPER = merge_char_classes(_upper + _uncased)

_units = ('km km² km³ m m² m³ dm dm² dm³ cm cm² cm³ mm mm² mm³ ha µm nm yd in ft '
          'kg g mg µg t lb oz m/s km/h kmh mph hPa Pa mbar mb MB kb KB gb GB tb '
          'TB T G M K % км км² км³ м м² м³ дм дм² дм³ см см² см³ мм мм² мм³ нм '
          'кг г мг м/с км/ч кПа Па мбар Кб КБ кб Мб МБ мб Гб ГБ гб Тб ТБ тб'
          'كم كم² كم³ م م² م³ سم سم² سم³ مم مم² مم³ كم غرام جرام جم كغ ملغ كوب اكواب')
_currency = r'\$ £ € ¥ ฿ US\$ C\$ A\$ ₽ ﷼ ₴'

# These expressions contain various unicode variations, including characters
# used in Chinese (see #1333, #1340, #1351) – unless there are cross-language
# conflicts, spaCy's base tokenizer should handle all of those by default
_punct = r'… …… , : ; \! \? ¿ ؟ ¡ \( \) \[ \] \{ \} < > _ # \* & 。 ？ ！ ， 、 ； ： ～ · । ، ؛ ٪'
_quotes = r'\' \'\' " ” “ `` ` ‘ ´ ‘‘ ’’ ‚ , „ » « 「 」 『 』 （ ） 〔 〕 【 】 《 》 〈 〉'
_hyphens = '- – — -- --- —— ~'

# Various symbols like dingbats, but also emoji
# Details: https://www.compart.com/en/unicode/category/So
_other_symbols = r'[\p{So}]'

UNITS    = split_chars(_units)
CURRENCY = split_chars(_currency)
QUOTES   = split_chars(_quotes)
PUNCT    = split_chars(_punct)
HYPHENS  = split_chars(_hyphens)
ICONS    = [_other_symbols]


