from nltk.corpus import wordnet as wn
from nltk import WordNetLemmatizer
lmtzr = WordNetLemmatizer()
#print lmtzr.lemmatize("eating")
fn=open("noun.txt","w")
noun={x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
for w in noun:
    fn.write(w)
    fn.write("\n")
if "i" in noun:
    print "true"
else:
    print "False"
