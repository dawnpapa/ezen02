from konlpy.tag import Okt
import re
from nltk.tokenize import word_tokenize
import nltk
nltk.download()

ctx="C:/Users/ezen/PycharmProjects/test02/data/"
filename=ctx+"kr-Report_2018.txt"

with open(filename,"r",encoding="UTF-8") as f:
    texts=f.read()

texts=texts.replace('\n','')
tokenizer=re.compile('[^ ㄱ-힣]+')
texts=tokenizer.sub('',texts)

tokens=word_tokenize(texts)
print(texts[:300])