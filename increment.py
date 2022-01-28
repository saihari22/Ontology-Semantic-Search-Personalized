#!C:\Users\Sairam\Anaconda3\python.exe
import sys
import os
import csv
import json
from tempfile import NamedTemporaryFile
import shutil
import csv
from pathlib import Path

link = sys.argv[1]
user=sys.argv[2]

filename = user+'.csv'
p="E:\\Xampp\\htdocs\\Ontology\\"+filename //add your path here
my_file = Path(p)

if my_file.exists():
    tempfile = NamedTemporaryFile(mode='w', delete=False,newline='')
    fields = ['url', 'visited_count']
    with open(filename,'r',newline='') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row['url'] == str(link):
                new_val=int(row['visited_count'],10)+1
                row['url'], row['visited_count'] = link, new_val
                row = {'url': row['url'], 'visited_count': row['visited_count']}
            writer.writerow(row)


    shutil.move(tempfile.name, filename)
else:
    with open(filename, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['url', 'visited_count'])
        filewriter.writerow([link,"1"])
