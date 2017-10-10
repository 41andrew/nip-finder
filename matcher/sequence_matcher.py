from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv



print (fuzz.partial_ratio("pkn orlen", "pkn orlen sp. z.o.o."))

print(fuzz.ratio("pkn orlen", "pkn orlen sp. zo.o.o"))

def similarity_checker(a, b):
    return fuzz.ratio(a, b)

def similarity_partial_checker(a, b):
    return fuzz.partial_ratio(a, b)

with open('entities_to_match.csv', encoding='windows-1250') as tomatch:
    reader = csv.reader(tomatch, delimiter=';')
    entities_to_match_list = list(reader)

with open('crm_entities.csv', encoding='windows-1252') as crm:
    reader = csv.reader(crm, delimiter=';')
    crm_entities_list = list(reader)

for x in entities_to_match_list:
    print ('Sprawdzam spółkę: ', x)
    for y in crm_entities_list:
        ratio = similarity_checker(x, y)
        if ratio > 87:
            print ('Spółka, którą sprawdzamy: ', x, ' jest podobna do spółki w CRM: ',y, ' z %:', ratio)
