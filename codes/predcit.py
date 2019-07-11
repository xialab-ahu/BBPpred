# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:55:13 2019

@author: ZQZ
"""

# import smtplib
import re, os, sys
import pandas as pd
from collections import Counter
# from email.header import Header
# from email.utils import formataddr
# from email.mime.text import MIMEText
from sklearn.externals import joblib
# from email.mime.multipart import MIMEMultipart
from Bio.SeqUtils.ProtParam import ProteinAnalysis

args = sys.argv

def readFasta(file):
	if os.path.exists(file) == False:
		print('Error: "' + file + '" does not exist.')
		sys.exit(1)

	with open(file) as f:
		records = f.read()

	if re.search('>', records) == None:
		print('The input file seems not in fasta format.')
		sys.exit(1)

	records = records.split('>')[1:]
	myFasta = []
	for fasta in records:
		array = fasta.split('\n')
		name, sequence = array[0].split()[0], re.sub('[^ARNDCQEGHILKMFPSTWYV-]', '-', ''.join(array[1:]).upper())
		myFasta.append([name, sequence])
	return myFasta


fastas = readFasta(args[1])

def AAC(fastas):
#	AA = kw['order'] if kw['order'] != None else 'ACDEFGHIKLMNPQRSTVWY'
	#AA = 'ARNDCQEGHILKMFPSTWYV'
    BBBAAC="HKPQR"
    encodings = []
    header = ['#Name']
              
    for i in BBBAAC:
        header.append(i)    
    encodings.append(header)

    for i in fastas:
        name, sequence = i[0], re.sub('-', '', i[1])
        count = Counter(sequence)
        for key in BBBAAC:
            count[key] = count[key]/len(sequence)
        code = [name]
        for aa in BBBAAC:
            code.append(count[aa])
        encodings.append(code)
    return encodings


def GAAC(fastas):
	group = {
		'alphatic': 'GAVLMI',
		'aromatic': 'FYW',
		'postivecharge': 'KRH',
		'negativecharge': 'DE',
		'uncharge': 'STCPNQ'
	}

	groupKey = group.keys()

	encodings1 = []
	header = []
	for key in groupKey:
		header.append(key)
	encodings1.append(header)

	for i in fastas:
		name, sequence = i[0], re.sub('-', '', i[1])
		code = []
		count = Counter(sequence)
		myDict = {}
		for key in groupKey:
			for aa in group[key]:
				myDict[key] = myDict.get(key, 0) + count[aa]

		for key in groupKey:
			code.append(myDict[key]/len(sequence))
		encodings1.append(code)

	return encodings1


def protein_length(fastas):
    encodings2 = []
    header = ["length"]
    encodings2.append(header)    
    for i in fastas:
        name, sequence = i[0], re.sub('-', '', i[1])
        code = []
        length=len(sequence)                
        Norlen=(length-5)/(82-5)
        code.append(Norlen)
        encodings2.append(code)
    return encodings2



def molecular_weight(fastas):
    #seq_new=seq.replace('X','').replace('B','')
    encodings3 = []
    header = ["Weight"]
    encodings3.append(header) 
    for i in fastas:
        name, sequence = i[0], re.sub('-', '', i[1]) 
        code = []             
        analysed_seq = ProteinAnalysis(sequence)
        analysed_seq.monoisotopic = True
        mw = analysed_seq.molecular_weight()
        Normw=(mw-513.222346)/(9577.017286-513.222346)
        code.append(Normw)
        encodings3.append(code)
    return(encodings3)
    



def savetsv(encodings, file = 'encoding.tsv'):
	with open(file, 'w') as f:
		if encodings == 0:
			f.write('Descriptor calculation failed.')
		else:
			for i in range(len(encodings[0])-1):
				f.write(encodings[0][i] + '\t')
			f.write(encodings[0][-1] + '\n')
			for i in encodings[1:]:
				f.write(i[0] + '\t')
				for j in range(1, len(i) - 1):
					f.write(str(float(i[j])) + '\t')
				f.write(str(float(i[len(i)-1])) + '\n')
	return None

myFun = "AAC(fastas)"
myFun1 = "GAAC(fastas)"
myFun2 = "protein_length(fastas)"
myFun3 = "molecular_weight(fastas)"

encodings = eval(myFun)
encodings1 = eval(myFun1)
encodings2 = eval(myFun2)
encodings3 = eval(myFun3)

  
encodings=ziped =list(map(lambda x:x[0]+x[1]+x[2]+x[3],zip(encodings,encodings1,encodings2,encodings3)))



RF=joblib.load('modeling')

PreData=pd.DataFrame(encodings[1:])
PreDataX=PreData.drop([0],axis=1) 
                        
result=RF.predict(PreDataX)

a=[]
for i in list(result):
    if i>0:
        a.append("bbb")
    else:
        a.append("non")
        
b=pd.DataFrame(list(zip(list(PreData[0]),a)))

b.columns = ['Name', 'predict']

b.to_csv(args[2],index=False,header=True)
