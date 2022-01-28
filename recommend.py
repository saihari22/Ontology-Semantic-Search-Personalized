#!C:\Users\Sairam\Anaconda3\python.exe
import csv
import spacy
import sys
import os
import codecs
import time
import requests
from time import sleep
import urllib3
import xlrd
from itertools import zip_longest
import urllib
import json
from pathlib import Path


user = sys.argv[1]
mylist = []

o = open("original.txt", 'r')
try:
    if os.stat("original.txt").st_size != 0:
       query = o.read().split()
       res = " "
    else:
       res = "No results found!"
except OSError:
    res = "original file missing!"

f = open("expansion.txt", 'r')
res = "No results found!"
try:
    if os.stat("expansion.txt").st_size != 0:
       word = f.read().split(") or (")
       res = " "
       for w in word:
            w = w.replace(")", "")
            w = w.replace("(", "")
            sub = w.split(" and ")
            for s in sub:
                    mylist.append(s)
    else:
        for i in query:
            mylist.append(i)
        res = "No results found!"
except OSError:
    res = "Expansion file missing!"

mylist = list(set(mylist))
stop=['is','from','has','in','has','of','by','made','to','2017','belongs','denoted','realeased','how','i','your','his','for','and']

expand=' '.join(mylist)
expand=expand.lower()
querywords = expand.split()
resultwords  = [word for word in querywords if word.lower() not in stop]
expand = ' '.join(resultwords)
query=' '.join(query)
query=query.lower()
query = query.split()
query = [word for word in query if word.lower() not in stop]
filename = "dataset.csv"
user_history=user+".csv"
no_of_urls=10
url = []
m=10
n=146
keyword = [[0]*m for i in range(n)]
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    i=0
    for row in csvreader:
        url.append(row[0])
        keyword[i]= row[1:]
        i=i+1

for i in range(len(keyword)):
    keyword[i]=' '.join(keyword[i])


nlp = spacy.load('en')
k=0
q=0
sum = [0 for x in range(n)]

expand=nlp(expand)
for i in keyword:
    for j in query:
        if i.find(j) != -1:
            sum[k]=sum[k]+0.5
    i=nlp(i)
    sum[k]=sum[k]+i.similarity(expand)
    k=k+1

index=(sorted(range(len(sum)), key=lambda k: sum[k])[::-1])

expand1=[]
for i in index:
    expand1.append(url[i])


p="E:\\Xampp\\htdocs\\Ontology\\"+user_history
my_file = Path(p)

if my_file.exists() and float(sum[index[0]])< (len(query)+1)*0.5:

    site_count = [[0]*1 for i in range(n)]
    top_url = [[0]*1 for i in range(n)]
    with open(user_history, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        i=0
        for row in csvreader:
            site_count[i]= int(row[1],10)
            top_url[i]=row[0]
            i=i+1


    count_new = [[0]*1 for i in range(no_of_urls)]
    url_new = [[0]*1 for i in range(no_of_urls)]

    for i in range(no_of_urls):
            count_new[i]=site_count[index[i]]
            url_new[i]=top_url[index[i]]


    def sort_list(list1, list2):
        zipped_pairs = zip(list2, list1)
        z = [x for _, x in sorted(zipped_pairs)]
        return z

    final=sort_list(url_new,count_new)
    final.reverse()
    print(final)
else:
    final=[]
    for i in range(no_of_urls):
        final.append(expand1[i])
    print(final)
