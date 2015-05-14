import re

from nltk.tokenize.punkt import PunktSentenceTokenizer


def preprocess(lines):
    for i in range(len(lines)):
        #lines[i]=lines[i].lower()
        #lines[i]='\n'.join(lines[i])
        # to remove html tags
        #lines[i]=self.strip_tags(lines[i])
        # to lower aplphabets
        try:
            #lines[i]=PunktSentenceTokenizer().tokenize(lines[i])
        
            #for j in range(len(lines[i])):
                lines[i] = lines[i].lower()
                #lines[i]='\n'.join(lines[i])
                
                
                #Convert www.* or https?://* to URL
                #lines[i] = re.sub('((www\.[\s]+)|(https?://[^\s]+))','',lines[i])
                #Remove additional white spaces
                #lines[i] = re.sub('[\s]+', ' ',lines[i])
                # remove underscores
                lines[i]=re.sub('_',' ', lines[i])
                # remove unicode and emoticons
                        
                #deal with truncated url
                #lines[i] = re.sub('(^|)?http?s?:?/?/?*?( |$)', '', lines[i])          #deal with compelted url
            
                lines[i] = re.sub(u'(RT |\\\\|\u201c)"?@*?[: ]', ' ', lines[i])        #deal with relines[i]
                lines[i] = re.sub('\.?@.*?( |:|$)', ' ', lines[i])                      #deal with username
                lines[i] = re.sub(r"\.\.+",' ',lines[i]) 
                #remove hash 
                lines[i] = re.sub('[][!"$*,/;<=>?@\\\\^_`{|}~]', '', lines[i])        #deal with punctu ion
                # remove special symbols
                lines[i] = re.sub('( - )', '', lines[i])
                lines[i] = re.sub('---', '', lines[i])
                lines[i] = re.sub('\.\.\.', ' ', lines[i])
                lines[i] = re.sub('(, |\.( |$))', ' ', lines[i])
                #lines[i] = re.sub("\S*\d\S*", " ", lines[i]).strip()
                lines[i]=re.sub(r'[^\x00-\x7F]','', lines[i])
                lines[i]=re.sub('@','',lines[i])
                lines[i]=re.sub(r'\\([^\s]+)','',lines[i])
                punctuation = re.compile(r'[-?!,":;()|$%&*+/<=>[\]^`{}~]')
                #Replace with space the punctuation 
                lines[i]=punctuation.sub('', lines[i])
                lines[i] = re.sub('&amp', '',lines[i])
                lines[i] = lines[i].strip('\'"')
        except UnicodeDecodeError:
            print "Unicode"
    return lines