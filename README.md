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

**Note:** If you close the terminal, but want to use the software again, you will need to run 
    
    cd ~/python3-spacy-tutorial
    source virt/bin/activate

### Test that everything installed correctly:
    python3 tutorial.py
    
The software should produce the following output:
        
    Sebastian Thrun PERSON
    Google ORG
    2007 DATE
    American NORP
    Thrun PERSON
    Recode ORG
    earlier this week DATE
    my fries were super gross such disgusting fries 0.7139701576579747



