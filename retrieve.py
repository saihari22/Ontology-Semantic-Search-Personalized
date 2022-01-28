import requests
import rdflib
from rdflib.plugins.sparql.processor import *
import sys
import rdflib
from rdflib.plugins.sparql.processor import *
import time
import os
import json
import json
import re

q=[]
t = time.time()
data = json.loads(sys.argv[1])
check=str(data)
fin=check.split()
for i in fin:
    i=i.replace("[","")
    i=i.replace("]","")
    i=i.replace(",","")
    i=i.replace("'","")
    q.append(i)

key_list=q
case = 0
if len(key_list) == 1:
    q ="""PREFIX dl: <http://ontology.dumontierlab.com/>
         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

       SELECT DISTINCT ?label ?plabel ?olabel ?comment
       WHERE{
        ?class rdfs:label ?label .
        ?class ?prop ?obj .
        ?obj rdfs:label ?olabel .
        ?prop rdfs:label ?plabel .
        OPTIONAL{?class rdfs:comment ?comment}
        FILTER(regex(?label,'""" + key_list[0].strip() + """',"i")) .
       }
       LIMIT 20"""
    case = 4
    resultsSub = requests.post('http://localhost:3030/combo/sparql', data={'query': q})

if case == 0:
    q ="""PREFIX dl: <http://ontology.dumontierlab.com/>
             PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

           SELECT DISTINCT ?label ?plabel ?olabel ?comment
           WHERE{
            ?class rdfs:label ?label .
            ?class ?prop ?obj .
            ?obj rdfs:label ?olabel .
            ?prop rdfs:label ?plabel .
            OPTIONAL{?class rdfs:comment ?comment}
            FILTER(regex(?label,'""" + key_list[1].strip() + """',"i") || regex(?label,'""" + key_list[0].strip() + """',"i")) .
           }
           LIMIT 20"""
    resultsSub = requests.post('http://localhost:3030/combo/sparql', data={'query': q})
    case = 1

if case == 0:
    q ="""PREFIX untitled-ontology-64: <http://www.semanticweb.org/vinu/ontologies/2014/3/untitled-ontology-64#>
         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

       SELECT DISTINCT ?label ?plabel ?olabel
       WHERE{
        {
            ?class rdfs:label ?label .
            ?class ?prop ?obj .
            ?obj rdfs:label ?olabel .
            ?prop rdfs:label ?plabel .
            FILTER( regex(?label,'""" + key_list[1].strip() + """',"i") || regex(?label,'""" + key_list[0].strip() + """',"i")) .
        }
          UNION
        {

            ?class rdfs:label ?label .
            ?class ?prop ?obj .
            ?obj rdfs:label ?olabel .
            ?prop rdfs:label ?plabel .
            FILTER( regex(?label,'""" + key_list[1].strip() + """',"i") || regex(?label,'""" + key_list[0].strip() + """',"i")) .
        }
       }
       LIMIT 10"""
    resultsSub=requests.post('http://localhost:3030/combo/sparql', data={'query': q})
    case = 2

if case == 0:
    q ="""PREFIX dl: <http://ontology.dumontierlab.com/>
         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

       SELECT DISTINCT ?label ?plabel ?olabel
       WHERE{
        {
            ?class rdfs:label ?label .
            ?class ?prop ?obj .
            ?obj rdfs:label ?olabel .
            ?prop rdfs:label ?plabel .
            FILTER( regex(?olabel,'""" + key_list[1].strip() + """',"i") || regex(?label,'""" + key_list[0].strip() + """',"i")) .
        }
          UNION
        {
            ?class rdfs:label ?label .
            ?class ?prop ?obj .
            ?obj rdfs:label ?olabel .
            ?prop rdfs:label ?plabel .
            FILTER( regex(?label,'""" + key_list[1].strip() + """',"i") || regex(?olabel,'""" + key_list[0].strip() + """',"i")) .
        }
       }
       LIMIT 20"""
    resultsSub= requests.post('http://localhost:3030/combo/sparql', data={'query': q})
    case = 3
if case == 3 and len(resultsSub) == 0:
    case = 100

for key1,val1 in d.items():
    if key1 =="results":
        for key2,val2 in val1.items():
                test=str(val2)
                for key in val2:
                    expString=str(key)
expQuery = set()



def ExpandQuery(case, resultsSub):
    if case == 1:
        expQuery = set()
        for row in resultsSub:
              q = "(" +" and ".join([row["label"]["value"],row["plabel"]["value"]]) +")"
              expQuery.add(q)
              q = "(" +" and ".join([row["label"]["value"],row["olabel"]["value"]]) +")"
              expQuery.add(q)
    elif case == 2:
        expQuery = set()

        for row in resultsSub:
              q = "(" +" and ".join([row["label"]["value"],row["plabel"]["value"]]) +")"
              expQuery.add(q)
              q = "(" +" and ".join([row["plabel"]["value"],row["olabel"]["value"]]) +")"
              expQuery.add(q)
    elif case == 3:
        expQuery = set()

        for row in resultsSub:
              q = "(" +" and ".join([row["label"]["value"],row["plabel"]["value"]]) +")"
              expQuery.add(q)
              q = "(" +" and ".join([row["plabel"]["value"],row["olabel"]["value"]]) +")"
              expQuery.add(q)
    elif case == 4:
        expQuery = set()
        for row in resultsSub:
             q = "(" +" and ".join([row["label"]["value"],row["plabel"]["value"]]) +")"
             expQuery.add(q)
             q = "(" +" and ".join([row["plabel"]["value"],row["olabel"]["value"]]) +")"
             expQuery.add(q)
    else:
        expQuery = "No result"
    return " or ".join(expQuery)

if case != 100:
    expand = ExpandQuery(case, val2)
    e = open("expansion.txt", 'w+')
    e.write(expand)
    e.close()
