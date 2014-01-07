#!/bin

#
#	About this file: In this script we are tokenizing the documents and observing the top words in the complete set of documents.
#


import nltk
import os
import operator
import random
	
resourcedir="/home/jayant/clipcard/resources"

def loadResources():
	STOPWORDS_FILE='stopwords.en'
	file_content=open(resourcedir + '/' + STOPWORDS_FILE).read()
	STOPWORDS=nltk.word_tokenize(file_content)
#	print(str(len(STOPWORDS)))
	return STOPWORDS

def tokenize(STOPWORDS):
	label={}
	rootdir = "/home/jayant/clipcard/dataset/parliament-debates"
	tf={} #term frequency array.
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			random.seed()
			newlabel=random.randint(0,1)
			label[subdir+'/'+file]=newlabel
			file_content = open(subdir+'/'+file).read()
			tokens=nltk.word_tokenize(file_content)
			for token in tokens:
				token=token.lower()
				if not token in STOPWORDS:
					if(tf.has_key(token)):
						tf[token]+=1
					else:
						tf[token]=0
			print file+' : '+str(len(tf))
	sorted_tf=sorted(tf.iteritems(), key=operator.itemgetter(1), reverse=True)
	for i in range(0,10):
		print(sorted_tf[i])

if __name__ == "__main__":
	STOPWORDS=loadResources()
	print('Number of stopwords :' + str(len(STOPWORDS)))
	tokenize(STOPWORDS)
