import pandas as pd
import os
import csv

file = 'transcriptions.csv'

#create a new text file with the text column (utf8)
with open(file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        with open('transcriptions.txt', 'a', encoding='utf-8') as f:
            f.write(row[1] + '\n')