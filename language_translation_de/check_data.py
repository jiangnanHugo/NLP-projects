import os
import sys
import gzip
import time
import codecs
import random
import pickle
import operator
import argparse
import numpy as np
from collections import defaultdict

def parseCorpus():

	with open("data/vocab.mdl", "rb") as model:
		[vocab, rVocab] = pickle.load(model)    

	with open("data/data_no_test_zip.mdl", "rb") as model:
		[x,y] = pickle.load(model)  
	
	for i in range(100):
		#if(len(x[i])>100):
		#		print len(x[i])
		l=[]
		print x[i]
		for j in range (len(x[i])):
			l.append(rVocab[x[i][j]].decode('utf8'))
		print(l)
		print y[i]	


		
		
	
	
	
parseCorpus()



