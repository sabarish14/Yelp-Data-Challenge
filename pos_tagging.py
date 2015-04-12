from nltk.tag.hunpos import HunposTagger
from file_read import file_read_text
import nltk
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
stopset = set(stopwords.words('english'))
lmtzr = WordNetLemmatizer()
def pos_tag(lines):
    #fp=open(name)
    vocab={}
    #lines=lines[1:10]
   
    ht = HunposTagger('en_wsj.model')
    adjective=file_read_text("adjective.txt")
    noun=file_read_text("noun.txt")
    wc=0
    '''for sentences in lines:
        for  line in sentences:
                    pos_tagged_lines.append(ht.tag(line.split()))'''
    '''for sentences in lines:
        for line in sentences:
        
            tokens = nltk.word_tokenize(line)
            filteredWords = [word for word in tokens if word not in stopset]
            
            tagged_text = ht.tag(filteredWords)
            for word, tag in tagged_text:
                if tag in ['NN','NNS']:
                    word=lmtzr.lemmatize(word)
                    if word not in vocab.keys() and word not in adjective and len(word)>3 and word  in noun:
                            vocab[word]=wc
                            wc+=1'''
    i=0
  
    for line in lines:
        new_line=""
        tokens = nltk.word_tokenize(line)
        filteredWords = [word for word in tokens if word not in stopset]
        
        tagged_text = ht.tag(filteredWords)
        
        for word, tag in tagged_text:
            if tag in ['NN','NNS']:
                word=lmtzr.lemmatize(word)
                if word not in vocab.keys() and word not in adjective and len(word)>3 and word  in noun:
                        new_line+=word+" "
                        #vocab[word]=wc
                        #wc+=1
        lines[i]=new_line
        i+=1
    '''for sentences in lines:
        for  line in sentences: 
            for w in line.split():
                        if w in noun and len(w)>3: 
                            #print noun.index(w)
                            if w not in vocab.keys():
                                vocab[w]=wc
                                wc+=1''' 
                                 
    #print pos_tagged_lines
    
    #noun_words=Set(vocab)
    return lines
                
            