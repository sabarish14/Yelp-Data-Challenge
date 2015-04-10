from nltk.tag.hunpos import HunposTagger

def pos_tag(lines):
    #fp=open(name)
    vocab={}
    #lines=lines[1:10]
    pos_tagged_lines=[]
    ht = HunposTagger('en_wsj.model')
    
    
    wc=0
    for sentences in lines:
        for  line in sentences:
            pos_tagged_lines.append(ht.tag(line.split()))
            
    #print pos_tagged_lines
    for line in pos_tagged_lines:
        #print lines,"\n"
        for tuples in line:
            if tuples[1]=='NN':
                w=tuples[0]
                if w not in vocab.keys():
                    vocab[w]=wc
                    wc+=1
    #noun_words=Set(vocab)
    return vocab
                
            