from simple_nlp_mmg import STOPLIST, SYMBOLS, nlp

class simple_nlp:
    
    def __init__(self, text):
        self.text         = text
        self.doc          = nlp(text)
        self.clean_text   = ''     
        self.sentence_num = []
        self.tags         = []
        self.tokens       = []
        self.entity       = []
        self.dependencies = []
        self.pos          = [] 
        self.lemma        = []
        self.is_stop      = []
        self.length       = [] 
        self.is_alpha     = []
        self.cluster      = []
        self.prob         = []
        self.children     = []

    def preprocess(self, to_lower = True, stoplist = STOPLIST, symbols = SYMBOLS):
        #------------------------------------------------------------------------
        # Generate clean-text
        #------------------------------------------------------------------------
        # get rid of newlines
        self.clean_text = self.text.strip().replace("\n", " ").replace("\r", " ")
            
        # replace HTML symbols
        self.clean_text = self.clean_text.replace("&amp;", "and").replace("&gt;", ">").replace("&lt;", "<")

        # lowercase
        if to_lower == True:
            self.clean_text = self.clean_text.lower()

        #------------------------------------------------------------------------
        # cast the data to a spacy type
        #------------------------------------------------------------------------
        doc   = nlp(self.clean_text)
        sents = list(doc.sents)

        #------------------------------------------------------------------------
        # remove stopwords, and store as as list of lists.
        #------------------------------------------------------------------------
        # for each sentence.
        sent_tokens = []
        for sent in sents:
            
            # remove stoplist tokens
            toks = [str(tok) for tok in sent if str(tok) not in stoplist]

            # remove symbols
            toks = [tok for tok in toks if tok not in symbols]

            # remove large strings of whitespace
            while "" in toks:
                toks.remove("")
            while " " in toks:
                toks.remove(" ")
            while "  " in toks:
                toks.remove("  ")
            while "   " in toks:
                toks.remove("   ")
            while "    " in toks:
                toks.remove("    ")
            while "\t" in toks:
                toks.remove("\t")
            while "\n" in toks:
                toks.remove("\n")
            while "\n\n" in toks:
                toks.remove("\n\n")
            
            sent_tokens.append(toks)
        
        clean_text = ''
        sentence_num, tokens = [], []
        for i,sent in enumerate(sent_tokens):
            for word in sent:
                sentence_num.append(i)
                tokens.append(word)
                clean_text += word + ' '
            clean_text = clean_text[:-1] + ' . '

        child_list = []
        for token in self.doc:
            children = []
            for child in token.children:
                children += [child]
            child_list.append(children)
        
        self.doc          = nlp(clean_text)
        self.tokens       = tokens
        self.sentence_num = sentence_num
        self.clean_text   = clean_text
        self.children     = child_list 
        self.tags         = [token.tag_ for token in self.doc]
        self.dependencies = [token.dep_ for token in self.doc]
        self.pos          = [token.pos_ for token in self.doc] 
        self.lemma        = [token.lemma_ for token in self.doc]
        self.is_stop      = [token.is_stop for token in self.doc]
        self.length       = [len(token.shape_) for token in self.doc] 
        self.is_alpha     = [token.is_alpha for token in self.doc]
        self.prob         = [token.prob for token in self.doc]
        self.cluster      = [token.cluster for token in self.doc]
        self.entity       = [entity.label_ for entity in self.doc.ents]
        self.ents         = [e.ent_type_ for e in self.doc]


        




# #-------------------------------------------------------------------------
# # Brown Cluster - places words in similar context in similar groups.
# #-------------------------------------------------------------------------
# text = u'Apples stocks dropped dramatically after the death of Steve Jobs in October and September' 
# doc  = nlp(text)

# for token in doc:
#     print('Custer #', token.cluster,',', token)

# print('-----------------------------------------------------------------')

# #-------------------------------------------------------------------------
# # Let's look at the dependencies of this example:
# #-------------------------------------------------------------------------
# example = "The boy with the spotted dog quickly ran after the firetruck."
# parsedEx = parser(example)
# # shown as: original token, dependency tag, head word, left dependents, right dependents
# for token in parsedEx:
#     print(token.orth_, token.dep_, token.head.orth_, [t.orth_ for t in token.lefts], [t.orth_ for t in token.rights])

        