
from HTMLParser import HTMLParser
import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize.punkt import PunktSentenceTokenizer

from pos_tagging  import pos_tag


english_stops = set(stopwords.words('english'))
english_stops.remove("no");
english_stops.remove("nor");
english_stops.remove("not");



#stemmer = PorterStemmer()

lmtzr = WordNetLemmatizer()

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
class preprocess:
    featurelist=[] 
    #start process_tweet
    
    def strip_tags(self,html):
        s = MLStripper()
        s.feed(html)
        return s.get_data()
    
   
           
    
    def extract_features(self,tweet):
        tweet_words = set(tweet)
        features = {}
        for word in self.featurelist:
            features['contains(%s)' % word] = (word in tweet_words)
        return features
        
    # function to preprocess    
    def preprocessin(self,cell_value):        
        # to tokenize the tweet into sentences
        tweet=PunktSentenceTokenizer().tokenize(cell_value)
        # to remove 'u'
        tweet='\n'.join(tweet)
        # to remove html tags
        tweet=self.strip_tags(tweet)
        # to lower aplphabets
        tweet = tweet.lower()
        
        
        #Convert www.* or https?://* to URL
        tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','',tweet)
        #Remove additional white spaces
        tweet = re.sub('[\s]+', ' ',tweet)
        # remove underscores
        tweet=re.sub('_',' ', tweet)
        #Replace rtword with word
        tweet = re.sub(r'rt([^\s]+)', r'\1', tweet)
        #remove @ words
        tweet = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet)
        # remove if seperate RT
        tweet = re.sub('rt', ' ', tweet)
        # remove unicode and emoticons
        tweet = re.sub(u'\u2026', ' ', tweet)                             #deal with horizontal ellipsis
        tweet = re.sub(u'[\u201c\u201d]', '"', tweet)                     #deal with double quotation mark
        tweet = re.sub(u'[\u2018\u2019]', '\'', tweet)                    #deal with single quotation mark
        #deal with truncated url
        tweet = re.sub('(^|)?http?s?:?/?/?.*?( |$)', ' ', tweet)          #deal with compelted url
    
        #tweet = re.sub(u'(RT |\\\\|\u201c)"?@.*?[: ]', ' ', tweet)        #deal with retweet
        #tweet = re.sub('\.?@.*?( |:|$)', ' ', tweet)                      #deal with username
        tweet = re.sub(r"\.\.+",' ',tweet) 
        #remove hash 
        tweet = re.sub('[][!"$*,/;<=>?@\\\\^_`{|}~]', ' ', tweet)        #deal with punctu ion
        # remove special symbols
        tweet = re.sub('( - )', ' ', tweet)
        tweet = re.sub('---', ' ', tweet)
        tweet = re.sub('\.\.\.', ' ', tweet)
        tweet = re.sub('(, |\.( |$))', ' ', tweet)
        #tweet = re.sub("\S*\d\S*", " ", tweet).strip()
        tweet=re.sub(r'[^\x00-\x7F]',' ', tweet)
        tweet=re.sub('@',' ',tweet)
        tweet=re.sub(r'\\([^\s]+)',' ',tweet)
        punctuation = re.compile(r'[-.?!,":;()|$%&*+/<=>[\]^`{}~]')
        #Replace with space the punctuation 
        tweet=punctuation.sub(' ', tweet)
        tweet = re.sub('&amp', ' ',tweet)
        tweet = tweet.strip('\'"')
        
        return tweet
    
    def extractdata(self,worksheet,start,end,word_file_name,label_file_name):
            
        num_rows = end-1
       
        
        curr_row = start
        
        fs=open(label_file_name,"w")
        fo=open(word_file_name,"w")
        fb=open("business_id.txt","w")
        prev=""
        while curr_row <= num_rows:
            
           
            
           
                
            business_id=worksheet.cell_value(curr_row,0)
            cell_value = worksheet.cell_value(curr_row, 1)
            
            
            #print cell_value
            sentiment=worksheet.cell_value(curr_row, 2)
            curr_row += 1
            if prev==cell_value:
                continue
            prev=cell_value
                #tweet=cell_value
                
            
            
            tuples=[]
            #ignore mixed sentiment
           
            if sentiment==-1 or sentiment==1:
                pos_tuple=[]
                tweet=self.preprocessin(cell_value)
                #pos_tuple=pos_tag(tweet)
                tuples=self.tokenizeword(tweet,pos_tuple)
                
                for x in tuples:
                    fo.write(x+",")
                #fo.write(" ")
                fb.write(str(business_id))
                fb.write("\n")
                fs.write(str(sentiment))
                fs.write("\n")
                fo.write("\n")
           
                
                
    #function to tokenize word
    def tokenizeword(self,tweet,pos_tuple):
        #for each sentence in tweet
        wor=tweet.split()
        tag_list=[]
        bagofwords=[]
        for j in wor:
            if j not in english_stops and  len(j)>=2:
                bagofwords.append(j)
        '''for word,tag in pos_tuple:
            #for word,tag in pos:
                tag_list.append(tag)
                
                
        pos_tags={"NN":"n","CC":"c","NNS":"n","JJ":"a","JJR":"a","JJS":"a","VB":"v","VBD":"v","VBG":"v","VBN":"v","VBP":"v","VBZ":"v"}
        
        
        for j,tag in zip(wor,tag_list):
                
            #if j not in english_stops:
                f=j   
               
                f=re.sub(r'(.)\1+', r'\1\1', f)
                try:
                    pos_word=pos_tags[tag]
                    if pos_word=="v" or pos_word=="a":
                        lmtzr.lemmatize(f,pos_word)
                    
                except KeyError:
                    #print 'err'
                    err=1'''
        #pos=nltk.pos_tag(bagofwords)
        return bagofwords    

            

    
        
    

    
    
    
    
    
