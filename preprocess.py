import re
from nltk.tokenize.punkt import PunktSentenceTokenizer
def preprocess(lines):
    for i in range(len(lines)):
        #lines[i][j]=lines[i][j].lower()
        #lines[i][j]='\n'.join(lines[i][j])
        # to remove html tags
        #lines[i][j]=self.strip_tags(lines[i][j])
        # to lower aplphabets
        lines[i]=PunktSentenceTokenizer().tokenize(lines[i])
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].lower()
            #lines[i][j]='\n'.join(lines[i][j])
            
            
            #Convert www.* or https?://* to URL
            #lines[i][j] = re.sub('((www\.[\s]+)|(https?://[^\s]+))','',lines[i][j])
            #Remove additional white spaces
            #lines[i][j] = re.sub('[\s]+', ' ',lines[i][j])
            # remove underscores
            lines[i][j]=re.sub('_',' ', lines[i][j])
            # remove unicode and emoticons
                    
            #deal with truncated url
            #lines[i][j] = re.sub('(^|)?http?s?:?/?/?*?( |$)', '', lines[i][j])          #deal with compelted url
        
            lines[i][j] = re.sub(u'(RT |\\\\|\u201c)"?@*?[: ]', ' ', lines[i][j])        #deal with relines[i][j]
            lines[i][j] = re.sub('\.?@.*?( |:|$)', ' ', lines[i][j])                      #deal with username
            lines[i][j] = re.sub(r"\.\.+",' ',lines[i][j]) 
            #remove hash 
            lines[i][j] = re.sub('[][!"$*,/;<=>?@\\\\^_`{|}~]', '', lines[i][j])        #deal with punctu ion
            # remove special symbols
            lines[i][j] = re.sub('( - )', '', lines[i][j])
            lines[i][j] = re.sub('---', '', lines[i][j])
            lines[i][j] = re.sub('\.\.\.', ' ', lines[i][j])
            lines[i][j] = re.sub('(, |\.( |$))', ' ', lines[i][j])
            #lines[i][j] = re.sub("\S*\d\S*", " ", lines[i][j]).strip()
            lines[i][j]=re.sub(r'[^\x00-\x7F]','', lines[i][j])
            lines[i][j]=re.sub('@','',lines[i][j])
            lines[i][j]=re.sub(r'\\([^\s]+)','',lines[i][j])
            punctuation = re.compile(r'[-?!,":;()|$%&*+/<=>[\]^`{}~]')
            #Replace with space the punctuation 
            lines[i][j]=punctuation.sub('', lines[i][j])
            lines[i][j] = re.sub('&amp', '',lines[i][j])
            lines[i][j] = lines[i][j].strip('\'"')
    return lines