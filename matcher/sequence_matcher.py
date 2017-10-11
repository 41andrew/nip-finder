from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class FuzzyMatcher:

    def __init__(self, entities_to_match_list, crm_entities, emis_entities):
        self.entities_to_match_list = entities_to_match_list
        self.crm_entities_to_match_list = crm_entities
        self.emis_entities_to_match_list = emis_entities

    def similarity_checker(self, a, b):
        return fuzz.ratio(a, b)

    def assign_objects_from_crm(self):

        for entity in self.entities_to_match_list:
            for entity_to_match in self.crm_entities_to_match_list:
                ratio = self.similarity_checker(entity, entity_to_match)
                print ("Porównuję spółkę ", entity, " ze spółką: ", entity_to_match, ". Podobieństwo to: ", ratio, "%")
                if (ratio > 90):
                    self.entities_to_match_list[entity].nip_list.append(self.crm_entities_to_match_list[entity_to_match])
                    print ("Do listy spółki ", entity, " dodaję obiekt: ", self.crm_entities_to_match_list[entity_to_match])


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
