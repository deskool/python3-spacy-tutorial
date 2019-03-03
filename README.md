# Spacy for Python3 Tutorial

### About The Software 
This is a simple tutorial for how to use [spacy](href="https://spacy.io) with Python3.

### Assumptions
This tutorial assumes:
1. That you are using a unix based system (the code should also work on a Mac).
2. That your system has Python 3 installed 

### Installation Instructions
To install the required packages for the software:
    
    cd ~
    git clone https://github.com/deskool/python3-spacy-tutorial.git
    cd python3-spacy-tutorial
    pip install virtualenv
    virtualenv virt
    source virt/bin/activate
    pip install -r requirements.txt
    python3 -m spacy download en
    python3 -m spacy download en_core_web_lg
    python3 -c  'import nltk;nltk.download("stopwords")'

**Note:** If you close the terminal, but want to use the software again, you will need to run 
    
    cd ~/python3-spacy-tutorial
    source virt/bin/activate

### Test that everything installed correctly:
    python3 test.py


### Questions?
Please email me.


## Some Regular Expressions
| Pattern | Behavior |
|---|---|
| . | Wildcard, matches any character |
| ^abc | Matches some pattern abc at the start of a string |
| abc$ | Matches some pattern abc at the end of a string |
| [abc] | Matches one of a set of characters |
| [A-Z0-9] | Matches one of a range of characters |
| ed|ing|s | Matches one of the specified strings (disjunction) |
| * | Zero or more of previous item, e.g. a*, [a-z]* (also known as Kleene Closure) |
| + | One or more of previous item, e.g. a+, [a-z]+ |
| ? | Zero or one of the previous item (i.e. optional), e.g. a?, [a-z]? |
| {n} | Exactly n repeats where n is a non-negative integer |
| {n,} | At least n repeats |
| {,n} | No more than n repeats |
| {m,n} | At least m and no more than n repeats |
| a(b|c)+ | Parentheses that indicate the scope of the operators |

