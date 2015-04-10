from nltk.corpus import wordnet as wn
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
    #nouns = wn.all_synsets('n') 
    #vocab=Set(vocab)
    feature_vector=[[0 for i in range(len(vocab))]for j in range(len(lines))]
    print len(feature_vector)
    for i  in range(len(lines)):
        #print "i",i
        for j in range(len(lines[i])):
            words=lines[i][j].split()
            for w in words:
                if w in vocab.keys():
                    feature_vector[i][vocab[w]]=1
    vocab=vocab.keys()
    for w in vocab:
        fv.write(w+"\n")
    return feature_vector,vocab
        
        
    