import sys
import csv
import re

if len(sys.argv) != 3:
    print("usage message")

# read dna sequence from txt file
with open(sys.argv[2], "r") as txt:
    dna = txt.read(-1)
# Opened database form csvfile
with open(sys.argv[1], "r") as database:
    # Opened as dictionary just to get the key
    dnaread = csv.DictReader(database)
    for row in dnaread:
        i = list(row)
        break
    i = i[1:]
    # created empty dic to store value of given sample i txt file
    dic = {}  
    for element in i:
        result = re.findall(f"(?:{element})+", dna)
        if result: 
            dic[element] = str(int(len(max(result)) / len(element)))
# Opening twice becoz first element missing, when not opened again.          
with open(sys.argv[1], "r") as database:
    dnaread = csv.DictReader(database)            
    for row in dnaread:
        a = dict(row)
        del a["name"]
        # matched if both dictionaries are same or not
        if a == dic:
            print(row["name"])
            break
    else:
        print("No match")