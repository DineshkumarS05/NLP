"""
#pip install nltk  if not installed from this way uninstall nltk and install using next line.
#pip install -U nltk
import nltk
import os  #we can use it to access our system.
import nltk.corpus  #it is the documentation 
"""

"""
print(os.listdir(nltk.data.find('corpora')))
#to check the fields associated in a file gutenberg
print(nltk.corpus.gutenberg.fileids())
#now we are picking a file from it
saks=nltk.corpus.gutenberg.words("shakespeare-hamlet.txt")
#checking the content of the file
for word in saks[0:100]:
    print(word,end=' ')
"""

#1) Tokenization
#to tokenize the sentence use
from nltk.tokenize import word_tokenize as wt
a1='''this is the first paragraph.
hello how are You. i am good sir what about you'''
a=a1.lower()
a=wt(a)


strCollect=[]
for count in saks[:100]:
    strCollect.append(count)
strCollect=' '.join(strCollect)
strLower=strCollect.lower()
strToken=wt(strLower)    


"""
#to find out the frequency of distinct elements
from nltk.probability import FreqDist
b=FreqDist(strToken)
#frequency dist is a format similar to dictionary
#finding the most repeated values

c=b.most_common(4)

"""
"""
#key terms in tokenizer are: bigrams(groups of two consecutive words)
#trigrams(groups of three consecutive words),ngrams(groups of n consecutive words)
from nltk.util import bigrams,trigrams,ngrams
bi=list(bigrams(a))
tri=list(trigrams(a))
ng=list(ngrams(a,5))
"""

"""
#2 Stemming: normalizing the words into their normal or root form
from nltk.stem import PorterStemmer
ste=PorterStemmer()
st1=ste.stem("having")
"""
"""
#importing multi values for finding their stemmer
from nltk.stem import PorterStemmer as ps
dat=['given','giving','give','gave']
ste=ps()
for i in dat:
    print(ste.stem(i))
#result is given give give give it means ing removed
"""
"""
#next stemmer is LancasterStemmer: more powerful
from nltk.stem import LancasterStemmer as ls
dat=["given","giving","give","gave"]
lst=ls()
for i in dat:
    print(lst.stem(i))
    #more agressive than porter
"""
"""
#3 parts of speech: tags defining
from nltk.tokenize import word_tokenize as wt
import nltk
String="hello how are you sir I am fine"
tkn=wt(String)
aa=[]
for token in tkn:
    aa.append(nltk.pos_tag([token]))
	#print(nltk.pos_tag([token]))
"""

"""
#word lemmatizer:works similar as stemmer but it makes actual root form of a word
# Lemmatize with POS Tag
import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "V": wordnet.VERB,
                "N": wordnet.NOUN,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


lemmatizer = WordNetLemmatizer()

sentence = "The striped bats are hanging on their feet for best"

#tag,tag_dict=get_wordnet_pos('stripped')
print([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(sentence)])


#Read in re: sub,compile,search,group,children,fetch,fetchall,findall,find
"""

"""
#for it first download: nltk.download('stopwords')
from nltk.corpus import stopwords
print(stopwords.words('english'))
len(stopwords.words('english'))
"""

"""
"""


"""
#name entity recognition
from nltk import ne_chunk
import numpy as np
from nltk.tokenize import word_tokenize as wt
import nltk
String="The US President stays in the WHITE HOUSE."
Tkn=wt(String)
Pos=nltk.pos_tag(Tkn)
Chunk=ne_chunk(Pos)
print(Chunk)
"""

#chunking: grouping individual information into bigger pieces.
from nltk.tokenize import word_tokenize as wt

import nltk
String="The big cat ate the little mouse who was after fresh cheese."
tkn=wt(String)
pos=nltk.pos_tag(tkn)
#using re making rule of program
Grammer_np=r"NP:  {<DT><JJ><NN>}"
Chunk_Parser=nltk.RegexpParser(Grammer_np)
#Now we have to pass the chunk so parse will be used as shown below:-
Chunk_result=Chunk_Parser.parse(pos)
