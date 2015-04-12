from nltk.corpus import wordnet as wn
def filter_lines(lines,vocab):
    topic_words=[[]for i in range(len(lines))]
    for i  in range(len(lines)):
        
        for j in range(len(lines[i])):
            
            words=lines[i][j].split()
            for w in words:
                if w in vocab.keys():
                    topic_words[i].append(w)
                    
                
    return topic_words
def build_feature_vector(lines,vocab):
    '''vocab={}
    #lines=lines[1:10]
    wc=1
    for line in lines:
        words=line.split()
        for w in words:
            if w not in vocab.keys():
                vocab[w]=wc
                wc+=1'''
            
                
                
                
    fv=open("vocab.txt","w")  
         
    
    topic_words=filter_lines(lines, vocab)
    feature_vector=[[0 for i in range(len(vocab))]for j in range(len(lines))]
    print len(feature_vector)
    '''for i  in range(len(lines)):
        #print "i",i
        for j in range(len(lines[i])):
            words=lines[i][j].split()
            for w in words:
                if w in vocab.keys():'''
    for i  in range(len(topic_words)):
        for w in topic_words[i]:
                col=vocab[w]
                feature_vector[i][col]+=1
    vocab=vocab.keys()
    for w in vocab:
        fv.write(w+"\n")
    return feature_vector,vocab
        
        
    