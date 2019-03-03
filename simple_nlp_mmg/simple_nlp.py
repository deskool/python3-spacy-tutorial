from simple_nlp_mmg import STOPLIST, SYMBOLS, WHITESPACE, nlp
import pandas as pd

class simple_nlp:
    
    def __init__(self, text):
        
        self.text        = text
        self.clean_text  = ''
        self.doc         = nlp(text) 
        self.features    = pd.DataFrame()

    def process(self):

        #------------------------------------------------------------------------
        # cast the data to a spacy type
        #------------------------------------------------------------------------
        doc   = nlp(self.text)
        sents = list(doc.sents)

        #------------------------------------------------------------------------
        # Compute Features.
        #------------------------------------------------------------------------
        
        # SENTENCE NUMBER
        # Convert doc to list of lists.
        sent_tokens = []
        for sent in sents:
            toks = [str(tok) for tok in sent]
            sent_tokens.append(toks)
        
        # Get the sentence number:
        sentence_num, tokens = [], []
        for i,sent in enumerate(sent_tokens):
            for word in sent:
                sentence_num.append(i)
                tokens.append(word)
            
        # TOKEN CHILDREN
        child_list = []
        for token in self.doc:
            children = []
            for child in token.children:
                children += [child]
            child_list.append(children)

        children = child_list 

        # IS WHITESPACE
        is_whitespace = [True if str(token) in WHITESPACE else False for token in self.doc]
        
        # IS STOPWORD
        is_stop       = [True if str(token) in STOPLIST else False for token in self.doc]
        
        # IS SYMBOL
        is_symbol     = [True if str(token) in SYMBOLS else False for token in self.doc]
        
        # IS ALPHABETICAL STRING
        is_alpha      = [token.is_alpha for token in self.doc]
        
        # TAGS
        tags          = [token.tag_ for token in self.doc]
        
        # DEPENDENCIES
        dependencies  = [token.dep_ for token in self.doc]
        
        # PARTS OF SPEECH
        pos           = [token.pos_ for token in self.doc] 
        
        # LEMMA
        lemma         = [token.lemma_ for token in self.doc]  
        
        # WORD LENGTH
        length        = [len(token.shape_) for token in self.doc] 
        
        # PROBABILITIES
        prob          = [token.prob for token in self.doc]
        
        # BROWNIAN CLUSTER
        cluster       = [token.cluster for token in self.doc]
        
        # ENTITIY
        ents          = [e.ent_type_ for e in self.doc]


        #------------------------------------------------------------
        # Assign features
        #------------------------------------------------------------
        self.features    = pd.DataFrame({'tokens': tokens,
                                         'sentence_num': sentence_num,
                                         'tags': tags,
                                         'children': children,
                                         'dependencies': dependencies,
                                         'pos': pos,
                                         'lemma': lemma,
                                         'is_stop':is_stop,
                                         'is_whitespace': is_whitespace,
                                         'is_symbol': is_symbol,
                                         'length':length,
                                         'is_alpha':is_alpha,
                                         'prob': prob,
                                         'cluster':cluster,
                                         'entity':ents
                                        })
